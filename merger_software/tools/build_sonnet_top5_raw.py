#!/usr/bin/env python3
"""Rebuild top5_raw.md (five fenced python blocks) from candidate_1..5.py."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"


def build(pid: str) -> None:
    pdir = OUT / pid
    blocks = []
    for i in range(1, 6):
        code = (pdir / f"candidate_{i}.py").read_text().rstrip("\n")
        blocks.append(f"```python\n{code}\n```")
    (pdir / "top5_raw.md").write_text("\n\n".join(blocks) + "\n")


def main() -> int:
    pids = sys.argv[1:] or sorted(
        p.name for p in OUT.iterdir() if p.is_dir() and p.name != "codeforces_data"
    )
    for pid in pids:
        build(pid)
        print(f"wrote {pid}/top5_raw.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
