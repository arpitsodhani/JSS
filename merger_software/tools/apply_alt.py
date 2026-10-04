#!/usr/bin/env python3
"""Swap one clause body in one candidate for a differently-shaped implementation.

Reads the replacement clause (marker line included) on stdin, so a batch script
can pipe in the second algorithm for a problem without rewriting the file.

    apply_alt.py <pid> <candidate number> <clause name> < body.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "ast_merger_sonent_sols"


def main():
    pid, number, clause = sys.argv[1], sys.argv[2], sys.argv[3]
    path = ROOT / pid / f"candidate_{number}.py"
    text = path.read_text()
    start = text.index(f"# --- clause: {clause} ")
    after = text.find("# --- clause: ", start + 10)
    end = after if after >= 0 else len(text)
    path.write_text(text[:start] + sys.stdin.read() + text[end:])


if __name__ == "__main__":
    main()
