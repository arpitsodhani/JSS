#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def parse_problem_id(problem_id: str) -> tuple[str, str]:
    match = re.fullmatch(r"(\d+)([A-Za-z]\d*)", problem_id)
    if not match:
        raise SystemExit(f"Invalid Codeforces problem id: {problem_id}")
    return match.group(1), match.group(2).upper()


def candidate_sources(root: Path, problem_id: str, limit: int) -> list[str]:
    contest, index = parse_problem_id(problem_id)
    sources = []

    solution = root / "codeforces_sols" / problem_id / "solution.py"
    if solution.exists():
        sources.append(solution.read_text())

    fixture_key = f"cf{contest}_{index.lower()}"
    fixture_dir = root / "codeforces" / "fixtures" / "llm_cf"
    for path in sorted(fixture_dir.glob(f"codegen__{fixture_key}__*.json")):
        try:
            payload = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        source = payload.get("source_code")
        if source:
            sources.append(source)

    unique = []
    seen = set()
    for source in sources:
        normalized = source.strip()
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique.append(source if source.endswith("\n") else source + "\n")
        if len(unique) == limit:
            break

    return unique


def main() -> int:
    parser = argparse.ArgumentParser(description="Build UAST merger input for a Codeforces problem.")
    parser.add_argument("problem_id", help="Example: 1693B")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Testbed root")
    parser.add_argument("--limit", type=int, default=5, help="Maximum candidate programs")
    parser.add_argument("--out", type=Path, help="Output JSON path")
    args = parser.parse_args()

    root = args.root.resolve()
    sources = candidate_sources(root, args.problem_id, args.limit)
    if not sources:
        raise SystemExit(f"No candidates found for {args.problem_id}")

    payload = {
        "programs": [
            {
                "id": f"P{i}",
                "clauses": [
                    {
                        "clause_id": "program",
                        "signature": "python_module",
                        "code": source,
                    }
                ],
            }
            for i, source in enumerate(sources, 1)
        ]
    }

    out = args.out or root / "merger_inputs" / args.problem_id / "uast_input.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {out} with {len(sources)} candidate(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
