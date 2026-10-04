#!/usr/bin/env python3
"""Calibrate the UAST merger's clause-similarity metric and clustering threshold.

Builds a labelled pair set from ast_merger_sonent_sols:

  positive : two variants of the SAME clause of the SAME problem
             (the merger must cluster these together)
  negative : clauses from DIFFERENT problems, and different clauses of the
             same problem (the merger must NOT cluster these)

Then reports, for a range of thresholds, how many positives cluster (recall)
and how many negatives wrongly cluster (false-positive rate).
"""
from __future__ import annotations

import itertools
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MERGER = ROOT / "ast_merger_lang_agnostic"
sys.path.insert(0, str(MERGER))

from tools.parser_base import create_parser          # noqa: E402
from tools.normalize import ASTNormalizer            # noqa: E402
from tools.fingerprint import Fingerprinter          # noqa: E402
import tools.fingerprint as FP                       # noqa: E402

OUT = ROOT / "ast_merger_sonent_sols"
_ALIVE: list = []          # the TED cache is keyed on id(); never let a tree be freed


TUNED_ON = ["1223D", "1693B", "1715B", "180D", "2051F", "2084A", "519C", "534B", "801B", "985C"]


def load_groups(lang: str = "python", only: set | None = None):
    parser = create_parser(lang)
    norm = ASTNormalizer(lang)
    fpr = Fingerprinter(lang)
    groups: dict[tuple[str, str], list] = {}
    for pdir in sorted(p for p in OUT.iterdir() if p.is_dir() and p.name != "codeforces_data"):
        if only is not None and pdir.name not in only:
            continue
        data = json.loads((pdir / "uast_input.json").read_text())
        for prog in data["programs"]:
            for cl in prog["clauses"]:
                parsed = parser.parse_clause(cl)
                parsed.ast = norm.normalize_ast(parsed.ast)
                fp = fpr.compute_fingerprint(parsed.ast)
                _ALIVE.append(parsed.ast)
                _ALIVE.append(fp)
                groups.setdefault((pdir.name, cl["clause_id"]), []).append(fp)
    return groups


def build_pairs(groups, seed: int = 11, n_neg: int = 800):
    positives = [(a, b) for v in groups.values() for a, b in itertools.combinations(v, 2)]
    keys = list(groups)
    rng = random.Random(seed)
    negatives = []
    while len(negatives) < n_neg:
        k1, k2 = rng.sample(keys, 2)
        if k1 == k2:
            continue
        negatives.append((groups[k1][rng.randrange(5)], groups[k2][rng.randrange(5)]))
    return positives, negatives


def report(positives, negatives, score, label: str):
    FP._ted_cache.clear()
    pos = sorted(score(a, b) for a, b in positives)
    neg = sorted(score(a, b) for a, b in negatives)

    def pct(xs, q):
        return xs[min(len(xs) - 1, int(q * len(xs)))]

    print(f"\n=== {label} ===")
    print(f"positives (same clause, 5 variants) n={len(pos):4d}  "
          f"min {pos[0]:.3f}  p05 {pct(pos,0.05):.3f}  median {pct(pos,0.5):.3f}  max {pos[-1]:.3f}")
    print(f"negatives (unrelated clauses)       n={len(neg):4d}  "
          f"min {neg[0]:.3f}  median {pct(neg,0.5):.3f}  p95 {pct(neg,0.95):.3f}  max {neg[-1]:.3f}")
    gap = pct(pos, 0.05) - pct(neg, 0.95)
    print(f"separation (pos p05 - neg p95)      : {gap:+.3f}")
    print(f"{'thr':>5s} {'recall':>7s} {'FPR':>7s} {'Youden J':>9s}")
    best = None
    for i in range(40, 100, 2):
        thr = i / 100
        tpr = sum(1 for x in pos if x >= thr) / len(pos)
        fpr = sum(1 for x in neg if x >= thr) / len(neg)
        j = tpr - fpr
        if best is None or j > best[3]:
            best = (thr, tpr, fpr, j)
        if thr >= 0.60:
            print(f"{thr:5.2f} {tpr:7.3f} {fpr:7.3f} {j:9.3f}")
    print(f"best Youden J at threshold {best[0]:.2f}: recall {best[1]:.3f}, FPR {best[2]:.3f}")
    return pos, neg, best


def split_report(operating_point: float = 0.60):
    """Train/holdout check: is the tuned threshold overfitted to the problems it was tuned on?"""
    all_names = {p.name for p in OUT.iterdir() if p.is_dir() and p.name != "codeforces_data"}
    train = set(TUNED_ON) & all_names
    holdout = all_names - train
    if not holdout:
        print("no holdout problems present")
        return

    print(f"tuned on : {sorted(train)}")
    print(f"holdout  : {sorted(holdout)}")

    for label, names in (("TRAIN (threshold was tuned here)", train),
                         ("HOLDOUT (never seen by the tuning)", holdout),
                         ("COMBINED", all_names)):
        groups = load_groups(only=names)
        pos_pairs, neg_pairs = build_pairs(groups, n_neg=800)
        pos = sorted(a.similarity(b) for a, b in pos_pairs)
        neg = sorted(a.similarity(b) for a, b in neg_pairs)
        tpr = sum(1 for x in pos if x >= operating_point) / len(pos)
        fpr = sum(1 for x in neg if x >= operating_point) / len(neg)
        best = max(((t / 100,
                     sum(1 for x in pos if x >= t / 100) / len(pos)
                     - sum(1 for x in neg if x >= t / 100) / len(neg))
                    for t in range(30, 100)), key=lambda z: z[1])
        print(f"\n{label}  ({len(names)} problems, {len(pos)} pos / {len(neg)} neg pairs)")
        print(f"  at threshold {operating_point:.2f} : recall {tpr:.3f}  FPR {fpr:.3f}  J {tpr - fpr:.3f}")
        print(f"  its own optimum      : threshold {best[0]:.2f}  J {best[1]:.3f}")


def main() -> int:
    if "--split" in sys.argv:
        op = 0.60
        for a in sys.argv:
            if a.startswith("--at="):
                op = float(a.split("=", 1)[1])
        split_report(op)
        return 0
    groups = load_groups()
    positives, negatives = build_pairs(groups)
    report(positives, negatives, lambda a, b: a.similarity(b), "current similarity()")
    for name in ("_jaccard_similarity", "_feature_similarity"):
        report(positives, negatives, lambda a, b, n=name: getattr(a, n)(b), f"component: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
