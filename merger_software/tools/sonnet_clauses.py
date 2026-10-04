#!/usr/bin/env python3
"""Shared helpers: split a candidate file into includes + independent clauses.

A candidate file looks like:

    import sys

    # --- clause: read_input ---
    def read_input():
        ...

    # --- clause: main ---
    def main():
        ...

    if __name__ == "__main__":
        main()

Everything before the first marker is the include block. Each marker starts a
clause whose body runs until the next marker (or end of file). Every candidate of
a problem must declare the same clause ids in the same order, and each clause must
keep the same interface in every candidate, so that the merger may pick clause i
from one program and clause j from another and still assemble a working program.
"""
from __future__ import annotations

import re
from pathlib import Path

MARKER = re.compile(r"^#\s*---\s*clause:\s*(\w+)\s*(?:::\s*(.+?))?\s*---\s*$")


def split_clauses(path: Path) -> tuple[list[str], list[tuple[str, str]]]:
    """Return (include lines, [(clause_id, code)]). Signatures are dropped here."""
    includes, clauses = split_clauses_full(path)
    return includes, [(cid, code) for cid, _sig, code in clauses]


def split_clauses_full(path: Path) -> tuple[list[str], list[tuple[str, str, str]]]:
    """Return (include lines, [(clause_id, signature, code)]).

    A marker declares the clause id and, after ``::``, its interface:

        # --- clause: solve_case :: (n: int, p: list[int]) -> int ---

    The signature is the contract every candidate must honour, because the
    merger may take this clause from one program and its callers from another.
    """
    includes: list[str] = []
    clauses: list[tuple[str, str, str]] = []
    current_id: str | None = None
    current_sig: str = ""
    buffer: list[str] = []

    for line in path.read_text().splitlines():
        match = MARKER.match(line)
        if match:
            if current_id is not None:
                clauses.append((current_id, current_sig, "\n".join(buffer).strip("\n")))
            current_id = match.group(1)
            current_sig = (match.group(2) or "").strip()
            buffer = []
            continue
        if current_id is None:
            if line.strip():
                includes.append(line.rstrip())
        else:
            buffer.append(line)

    if current_id is not None:
        clauses.append((current_id, current_sig, "\n".join(buffer).strip("\n")))
    if not clauses:
        raise ValueError(f"{path}: no clause markers found")
    return includes, clauses


def clause_ids(path: Path) -> tuple[str, ...]:
    return tuple(cid for cid, _ in split_clauses(path)[1])


def clause_signatures(path: Path) -> tuple[tuple[str, str], ...]:
    return tuple((cid, sig) for cid, sig, _ in split_clauses_full(path)[1])
