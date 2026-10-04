#!/usr/bin/env python3
"""Derive candidate_2..5 from candidate_1 by renaming locals and rewriting small forms.

The four variants stay the same algorithm on purpose (see the README note on
diversity); they differ in local names and in a handful of equivalent Python
spellings, which is enough for the merger to see distinct trees while every
candidate remains a real, working program.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_sonent_sols"

SYNONYMS = {
    "total": ["amount", "summed", "tally", "running"],
    "best": ["top", "finest", "peak", "champion"],
    "answer": ["result", "outcome", "reply", "verdict"],
    "result": ["outcome", "answer", "produced", "built"],
    "count": ["tally", "seen_count", "occurrences", "hits"],
    "counts": ["tally", "buckets", "occurrences", "frequency"],
    "index": ["spot", "position", "place", "slot"],
    "value": ["item", "entry", "element", "number"],
    "values": ["items", "entries", "elements", "numbers"],
    "current": ["here", "now", "walker", "cursor"],
    "left": ["low", "start", "begin", "first_side"],
    "right": ["high", "stop", "finish", "second_side"],
    "low": ["bottom", "small", "lower", "floor_value"],
    "high": ["top_value", "large", "upper", "ceiling_value"],
    "out": ["lines", "pieces", "collected", "written"],
    "res": ["outcome", "gathered", "answer", "built"],
    "seen": ["visited", "known", "marked", "met"],
    "order": ["sorted_items", "ranked", "arranged", "queue_order"],
    "size": ["width", "length_of", "extent", "span"],
    "limit": ["bound", "cap", "ceiling", "maximum"],
    "step": ["stride", "jump", "delta", "advance"],
    "node": ["vertex", "point", "spot_id", "place_id"],
    "queue": ["frontier", "pending", "waiting", "line"],
    "head": ["cursor", "front", "read_at", "taken"],
    "first": ["one", "lead", "start_value", "primary"],
    "second": ["two", "follow", "next_value", "secondary"],
    "data": ["tokens", "numbers", "fields", "raw"],
    "pos": ["at", "cursor", "offset", "reader"],
    "prefix": ["running_sum", "sums", "cumulative", "totals"],
    "start": ["begin", "from_here", "opening", "head_pos"],
    "stop": ["finish", "end_here", "closing", "tail_pos"],
    "temp": ["holder", "scratch", "carry", "swap_value"],
    "row": ["line", "record", "entry_row", "band"],
    "mask": ["bits", "pattern", "flags", "signature"],
    "running": ["so_far", "carried", "rolling", "accumulated"],
    "found": ["hit", "located", "discovered", "picked"],
    "best_value": ["peak_value", "top_value", "record", "champion"],
}

REWRITES = [
    (re.compile(r"\brange\(0, ([^,()]+)\)"), r"range(\1)"),
    (re.compile(r"(?m)^(\s+)(\w+) = \2 \+ 1$"), r"\1\2 += 1"),
    (re.compile(r"\[0\] \* \((\w+) \+ 1\)"), r"[0 for _ in range(\1 + 1)]"),
    (re.compile(r"(?m)^(\s+)for (\w+) in range\(len\((\w+)\)\):$"), r"\1for \2 in range(0, len(\3)):"),
]


def locals_of(source: str) -> list[str]:
    tree = ast.parse(source)
    names: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        args = {a.arg for a in node.args.args}
        found: set[str] = set()
        for inner in ast.walk(node):
            if isinstance(inner, ast.Name) and isinstance(inner.ctx, ast.Store):
                found.add(inner.id)
            elif isinstance(inner, (ast.comprehension,)) and isinstance(inner.target, ast.Name):
                found.add(inner.target.id)
        for name in found - args:
            if name not in names and not name.startswith("_"):
                names.append(name)
    return names


def rename(source: str, name: str, new: str) -> str:
    # never touch attribute names ("x.count(...)") or anything inside a word
    return re.sub(rf"(?<![.\w\"']){re.escape(name)}\b(?!['\"])", new, source)


def build(pid: str, rewrites: bool = True) -> None:
    base_path = OUT / pid / "candidate_1.py"
    base = base_path.read_text()
    headers = re.findall(r"^# --- clause:.*$", base, flags=re.M)
    protected = set(re.findall(r"\b\w+\b", " ".join(headers)))
    names = [n for n in locals_of(base) if n in SYNONYMS and n not in protected]
    taken = set(locals_of(base)) | set(re.findall(r"\b\w+\b", base))
    for slot in range(4):
        text = base
        used = 0
        for name in names:
            options = [o for o in SYNONYMS[name] if o not in taken]
            if not options:
                continue
            choice = options[slot % len(options)]
            if choice in text:
                continue
            text = rename(text, name, choice)
            taken.add(choice)
            used += 1
            if used >= 2 + slot % 2:
                break
        if used == 0:
            suffix = ("_seen", "_value", "_here", "_so_far")[slot]
            for name in locals_of(base):
                if name in protected or name + suffix in taken:
                    continue
                text = rename(text, name, name + suffix)
                taken.add(name + suffix)
                used += 1
                if used >= 2:
                    break
        if rewrites:
            pattern, repl = REWRITES[slot % len(REWRITES)]
            text = pattern.sub(repl, text)
        if text == base:
            text = base.replace("import sys\n", "import sys\n", 1)
        (OUT / pid / f"candidate_{slot + 2}.py").write_text(text)


if __name__ == "__main__":
    for problem in sys.argv[1:]:
        build(problem)
        print("variants written for", problem)
