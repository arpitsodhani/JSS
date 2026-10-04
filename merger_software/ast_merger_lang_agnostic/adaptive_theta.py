#!/usr/bin/env python3
"""Null-distribution / p-value based clustering threshold for the composer.

The composer normally clusters a clause's 5 candidate fingerprints with one
fixed similarity_threshold (0.60) shared by every clause in every problem.
That number is a guess: it assumes 0.60 means the same thing for a two-line
`read_input` clause and for a 40-line DP. It does not -- boilerplate clauses
share idiom (`sys.stdin.buffer.read().split()`, list slicing, ...) even when
they come from unrelated problems, so their *accidental* similarity floor is
much higher than a bespoke algorithmic clause's.

This module estimates, empirically, what "accidental" similarity looks like
for each clause role, and turns that into a per-role threshold via a
p-value: theta_role = the (1 - alpha) quantile of the null distribution of
similarities between clauses that are known to be unrelated (same role,
different problem). A clause's five candidates only cluster together if
their similarity would be surprising (p <= alpha) under that null.

Two subcommands:
  build-null   -- sample unrelated clause pairs across many problems, write
                  the empirical null distribution + derived thetas to JSON.
  merge        -- run the ordinary evaluate_clauses.py pipeline, but override
                  composer.threshold per clause_id from the null-distribution
                  thetas instead of a single fixed value. Never regenerates
                  candidates; only changes which similarity counts as
                  "agreement" when clustering the (unchanged) candidates.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

from tools.parser_base import create_parser
from tools.normalize import ASTNormalizer
from tools.fingerprint import Fingerprinter
from tools.composer import Composer

IO_NAMES = {"read_input", "main"}


def role_of(clause_id: str) -> str:
    """read_input and main are boilerplate-shaped in almost every problem;
    everything else is bespoke algorithmic logic."""
    if clause_id in IO_NAMES:
        return clause_id  # "read_input" and "main" get their own null distributions
    return "logic"


def load_fingerprints(uast_path: Path, lang: str, fingerprinter: Fingerprinter,
                       normalizer: ASTNormalizer, parser) -> dict:
    """clause_id -> role -> list of (variant_id, fingerprint) for program P1 only.

    One variant per problem is enough to characterise "what does an unrelated
    clause of this role look like"; we are not re-deriving per-candidate
    agreement here, just the shape of the null.
    """
    data = json.loads(uast_path.read_text())
    programs = data.get("programs", [])
    if not programs:
        return {}
    prog = programs[0]  # P1
    out = {}
    for clause_data in prog.get("clauses", []):
        parsed = parser.parse_clause(clause_data)
        if not parsed.ast:
            continue
        parsed.ast = normalizer.normalize_ast(parsed.ast)
        fp = fingerprinter.compute_fingerprint(parsed.ast, normalize=True)
        out[parsed.clause_id] = fp
    return out


def build_null(problems_dir: Path, sample_size: int, pairs_per_bucket: int,
                seed: int, exclude: set[str]) -> dict:
    lang = "python"
    parser = create_parser(lang)
    normalizer = ASTNormalizer(lang)
    fingerprinter = Fingerprinter(lang)

    candidates = [
        p for p in sorted(problems_dir.iterdir())
        if p.is_dir() and (p / "uast_input.json").exists() and p.name not in exclude
    ]
    rng = random.Random(seed)
    rng.shuffle(candidates)
    chosen = candidates[:sample_size]

    # bucket -> list of (problem_id, fingerprint)
    buckets: dict[str, list] = defaultdict(list)
    for pdir in chosen:
        try:
            fps = load_fingerprints(pdir / "uast_input.json", lang, fingerprinter, normalizer, parser)
        except Exception:
            continue
        for clause_id, fp in fps.items():
            buckets[role_of(clause_id)].append((pdir.name, fp))

    rng2 = random.Random(seed + 1)
    result = {"sample_problems": len(chosen), "problems_used": [p.name for p in chosen], "buckets": {}}
    import time as _time
    for bucket, items in buckets.items():
        print(f"[{bucket}] {len(items)} clauses in bucket, sampling up to {pairs_per_bucket} pairs...",
              flush=True)
        if len(items) < 4:
            continue
        sims = []
        attempts = 0
        max_attempts = pairs_per_bucket * 20
        seen_pairs = set()
        t_bucket = _time.monotonic()
        while len(sims) < pairs_per_bucket and attempts < max_attempts:
            attempts += 1
            a, b = rng2.sample(items, 2)
            if a[0] == b[0]:
                continue  # same problem: not a clean "unrelated" pair
            key = tuple(sorted((a[0], b[0])))
            if bucket != "logic" and key in seen_pairs:
                # small buckets (read_input/main) exhaust quickly; allow resampling
                # once we've covered all distinct problem pairs at least once
                if len(seen_pairs) < len(items) * (len(items) - 1) // 2:
                    continue
            seen_pairs.add(key)
            sims.append(a[1].similarity(b[1]))
            if len(sims) % 50 == 0:
                print(f"  [{bucket}] {len(sims)}/{pairs_per_bucket} pairs, "
                      f"{_time.monotonic() - t_bucket:.1f}s elapsed", flush=True)
        print(f"[{bucket}] done: {len(sims)} pairs in {_time.monotonic() - t_bucket:.1f}s", flush=True)
        sims.sort()
        n = len(sims)
        if n == 0:
            continue

        def quantile(q):
            idx = min(n - 1, max(0, int(q * n)))
            return sims[idx]

        alphas = [0.10, 0.05, 0.02, 0.01]
        thetas = {f"alpha_{a}": quantile(1 - a) for a in alphas}
        result["buckets"][bucket] = {
            "n_pairs": n,
            "n_clauses_in_bucket": len(items),
            "mean": sum(sims) / n,
            "min": sims[0],
            "max": sims[-1],
            "p50": quantile(0.50),
            "p90": quantile(0.90),
            "p95": quantile(0.95),
            "p98": quantile(0.98),
            "p99": quantile(0.99),
            "thetas": thetas,
            "raw_sample": sims[:: max(1, n // 200)],  # thin sample for inspection/plotting
        }
    return result


def p_value(observed: float, null_sims_sorted: list) -> float:
    """Fraction of the null distribution >= observed similarity."""
    import bisect
    n = len(null_sims_sorted)
    if n == 0:
        return float("nan")
    idx = bisect.bisect_left(null_sims_sorted, observed)
    return (n - idx) / n


def adaptive_merge(uast_path: Path, out_path: Path, null_theta_path: Path,
                    alpha_key: str, report_path: Path | None) -> bool:
    from tools.parser_base import ParsedClause  # noqa: F401  (type documentation only)

    null_data = json.loads(null_theta_path.read_text())
    buckets = null_data["buckets"]
    theta_for_role = {role: info["thetas"][alpha_key] for role, info in buckets.items()}
    default_theta = buckets.get("logic", {}).get("thetas", {}).get(alpha_key, 0.60)

    lang = "python"
    parser = create_parser(lang)
    normalizer = ASTNormalizer(lang)
    fingerprinter = Fingerprinter(lang)
    composer = Composer(lang=lang, threshold=default_theta)

    data = json.loads(uast_path.read_text())
    parsed_programs = []
    for prog in data.get("programs", []):
        parsed_clauses = []
        for clause_data in prog.get("clauses", []):
            parsed = parser.parse_clause(clause_data)
            if parsed.ast:
                parsed.ast = normalizer.normalize_ast(parsed.ast)
            parsed_clauses.append(parsed)
        parsed_programs.append({"id": prog.get("id"), "clauses": parsed_clauses,
                                 "includes": prog.get("includes", [])})

    clause_groups = defaultdict(list)
    for prog in parsed_programs:
        for clause in prog["clauses"]:
            clause_groups[clause.clause_id].append(clause)

    merged_clauses = []
    report = {"alpha_key": alpha_key, "clauses": {}}
    for clause_id, variants in clause_groups.items():
        role = role_of(clause_id)
        theta = theta_for_role.get(role, default_theta)
        composer.threshold = theta
        merged = composer.merge_clause(clause_id, variants)
        merged_clauses.append(merged)

        # p-value of the achieved intra-cluster agreement against this role's null
        null_info = buckets.get(role)
        pval = None
        if null_info and len(merged.used_fragments) > 1:
            raw = null_info.get("raw_sample") or []
            if raw:
                pval = p_value(merged.agreement, sorted(raw))

        report["clauses"][clause_id] = {
            "role": role,
            "theta_used": theta,
            "confidence": merged.confidence,
            "agreement": merged.agreement,
            "used_fragments": merged.used_fragments,
            "p_value_vs_null": pval,
        }

    all_includes = data.get("global_includes", [])
    for prog in parsed_programs:
        all_includes.extend(prog.get("includes", []))
    unique_includes = list(dict.fromkeys(all_includes))
    final_program, _ = composer.resolve_conflicts(merged_clauses, unique_includes)
    out_path.write_text(final_program)

    if report_path:
        report_path.write_text(json.dumps(report, indent=2))
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    bn = sub.add_parser("build-null")
    bn.add_argument("--problems-dir", required=True)
    bn.add_argument("--sample-size", type=int, default=60)
    bn.add_argument("--pairs-per-bucket", type=int, default=3000)
    bn.add_argument("--seed", type=int, default=20260912)
    bn.add_argument("--exclude", nargs="*", default=[])
    bn.add_argument("--out", required=True)

    mg = sub.add_parser("merge")
    mg.add_argument("--input", required=True)
    mg.add_argument("--out", required=True)
    mg.add_argument("--null-theta", required=True)
    mg.add_argument("--alpha-key", default="alpha_0.02")
    mg.add_argument("--report", default=None)

    args = ap.parse_args()
    if args.cmd == "build-null":
        result = build_null(Path(args.problems_dir), args.sample_size, args.pairs_per_bucket,
                             args.seed, set(args.exclude))
        Path(args.out).write_text(json.dumps(result, indent=2))
        for bucket, info in result["buckets"].items():
            print(f"{bucket:12s} n_pairs={info['n_pairs']:5d} mean={info['mean']:.3f} "
                  f"p90={info['p90']:.3f} p95={info['p95']:.3f} p98={info['p98']:.3f} "
                  f"p99={info['p99']:.3f}  theta@0.02={info['thetas']['alpha_0.02']:.3f}")
        return 0
    else:
        ok = adaptive_merge(Path(args.input), Path(args.out), Path(args.null_theta),
                             args.alpha_key, Path(args.report) if args.report else None)
        return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
