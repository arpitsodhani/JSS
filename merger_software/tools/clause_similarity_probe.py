#!/usr/bin/env python3
"""Report, per clause, the pairwise structural similarity between the five
candidates and the confidence the merger will therefore assign.

Confidence is |largest cluster| / 5, and clustering is complete-linkage at the
python threshold (0.60). So a clause reads 1.00 only when all five candidates are
mutually within threshold, and 0.80 when exactly one is pushed out. Use this while
writing candidates to check that a clause lands where it was meant to land instead
of discovering it after the merge.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"
MERGER = ROOT / "ast_merger_lang_agnostic"
sys.path.insert(0, str(MERGER))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from sonnet_clauses import split_clauses_full  # noqa: E402
from tools.parser_base import create_parser  # noqa: E402
from tools.normalize import ASTNormalizer  # noqa: E402
from tools.fingerprint import Fingerprinter  # noqa: E402


def probe(pid: str, threshold: float | None = None) -> list[dict]:
    pdir = OUT / pid
    parser = create_parser("python")
    normalizer = ASTNormalizer("python")
    fingerprinter = Fingerprinter("python")
    if threshold is None:
        threshold = fingerprinter.config.get("cluster_threshold", 0.60)

    per_program = []
    for i in range(1, 6):
        _inc, clauses = split_clauses_full(pdir / f"candidate_{i}.py")
        per_program.append(clauses)

    rows = []
    for ci, (cid, _sig, _code) in enumerate(per_program[0]):
        fps = []
        for prog in per_program:
            parsed = parser.parse_clause({"clause_id": cid, "signature": "python_block", "code": prog[ci][2]})
            if parsed.ast:
                parsed.ast = normalizer.normalize_ast(parsed.ast)
            fps.append(fingerprinter.compute_fingerprint(parsed.ast))
        sims = [[1.0] * 5 for _ in range(5)]
        for a in range(5):
            for b in range(a + 1, 5):
                sims[a][b] = sims[b][a] = fps[a].similarity(fps[b])
        clusters = fingerprinter.cluster_fingerprints(fps, similarity_threshold=threshold)
        clusters.sort(key=len, reverse=True)
        rows.append({
            "clause": cid,
            "confidence": len(clusters[0]) / 5,
            "clusters": clusters,
            "min_sim": min(sims[a][b] for a in range(5) for b in range(a + 1, 5)),
            "sims": sims,
        })
    return rows


def summarise(low: list[dict]) -> str:
    if not low:
        return "all 1.00"
    return ", ".join(f"{r['clause']}={r['confidence']:.2f}" for r in low)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pids", nargs="*")
    ap.add_argument("--threshold", type=float, default=None)
    ap.add_argument("--matrix", action="store_true", help="print the full 5x5 similarity matrix")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    pids = args.pids or sorted(p.name for p in OUT.iterdir()
                               if p.is_dir() and p.name != "codeforces_data"
                               and (p / "candidate_1.py").exists())
    allrows = {}
    for pid in pids:
        rows = probe(pid, args.threshold)
        allrows[pid] = rows
        if args.json:
            continue
        low = [r for r in rows if r["confidence"] < 1.0]
        print(f"{pid:8s} avg {sum(r['confidence'] for r in rows) / len(rows):.2f}"
              f"  {summarise(low)}")
        for r in rows:
            print(f"    {r['clause']:18s} conf {r['confidence']:.2f}  min_pair_sim {r['min_sim']:.3f}  clusters {r['clusters']}")
            if args.matrix:
                for a in range(5):
                    print("       " + " ".join(f"{r['sims'][a][b]:.3f}" for b in range(5)))
    if args.json:
        print(json.dumps(allrows, indent=2, default=list))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
