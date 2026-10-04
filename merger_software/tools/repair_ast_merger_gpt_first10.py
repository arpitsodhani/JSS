#!/usr/bin/env python3
"""Repair the first 10 ast_merger_gpt candidate ensembles.

The old candidate files were syntactically valid but often not complete
runnable programs, which let the clause merger assemble undefined names.  This
script replaces candidate_1.py..candidate_5.py for the first 10 mergeable
problems with complete clausewise programs.
"""
from __future__ import annotations

import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_gpt"
BACKUP = OUT / f".backup_first10_repair_{time.strftime('%Y%m%d_%H%M%S')}"

PROBLEMS = [
    "1693B",
    "2084A",
    "180D",
    "985C",
    "519C",
    "1715B",
    "2051F",
    "534B",
    "801B",
    "1223D",
]

SOURCES: dict[str, str] = {
    "1693B": r'''
import sys


# CLAUSE: parse_test_cases
def read_ints():
    return list(map(int, sys.stdin.buffer.read().split()))


# CLAUSE: build_child_adjacency
def build_children(n, parents):
    children = [[] for _ in range(n)]
    for node, parent in enumerate(parents, start=1):
        children[parent - 1].append(node)
    return children


# CLAUSE: collect_node_limits
def read_bounds(data, pos, n):
    left = [0] * n
    right = [0] * n
    for i in range(n):
        left[i] = data[pos]
        right[i] = data[pos + 1]
        pos += 2
    return left, right, pos


# CLAUSE: aggregate_subtree_capacity
def compute_operations(n, children, left, right):
    operations = 0
    carry = [0] * n
    for node in range(n - 1, -1, -1):
        total = 0
        for child in children[node]:
            total += carry[child]

        # CLAUSE: trigger_or_propagate
        if total < left[node]:
            operations += 1
            carry[node] = right[node]
        else:
            carry[node] = min(total, right[node])
    return operations


# CLAUSE: emit_answers
def solve():
    data = read_ints()
    if not data:
        return
    pos = 1
    out = []
    for _ in range(data[0]):
        n = data[pos]
        pos += 1
        parents = data[pos:pos + n - 1]
        pos += n - 1
        left, right, pos = read_bounds(data, pos, n)
        out.append(str(compute_operations(n, build_children(n, parents), left, right)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
''',
    "2084A": r'''
import sys


# CLAUSE: parse_test_cases
def read_cases():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]] if data else []


# CLAUSE: check_parity_feasibility
def is_possible(n):
    return n % 2 == 1


# CLAUSE: anchor_largest_value
def start_permutation(n):
    return [n]


# CLAUSE: append_ascending_tail
def construct_permutation(n):
    ans = start_permutation(n)
    ans.extend(range(1, n))
    return ans


# CLAUSE: format_case_answer
def answer_for(n):
    if not is_possible(n):
        return "-1"
    return " ".join(map(str, construct_permutation(n)))


# CLAUSE: emit_answers
def solve():
    sys.stdout.write("\n".join(answer_for(n) for n in read_cases()))


if __name__ == "__main__":
    solve()
''',
    "180D": r'''
import sys


# CLAUSE: count_source_letters
def letter_counts(text):
    counts = [0] * 26
    for ch in text:
        counts[ord(ch) - 97] += 1
    return counts


# CLAUSE: build_sorted_suffix
def build_from_counts(counts):
    parts = []
    for i, count in enumerate(counts):
        if count:
            parts.append(chr(97 + i) * count)
    return "".join(parts)


# CLAUSE: try_raise_at_prefix
def best_after_raising(prefix, counts, target_char):
    target = ord(target_char) - 97
    for c in range(target + 1, 26):
        if counts[c]:
            counts[c] -= 1
            candidate = "".join(prefix) + chr(97 + c) + build_from_counts(counts)
            counts[c] += 1
            return candidate
    return None


# CLAUSE: scan_equal_prefix
def smallest_greater_anagram(source, target):
    counts = letter_counts(source)
    best = None
    prefix = []
    limit = min(len(source), len(target))
    for i in range(limit):
        raised = best_after_raising(prefix, counts, target[i])
        if raised is not None and (best is None or raised < best):
            best = raised
        need = ord(target[i]) - 97
        if counts[need] == 0:
            break
        counts[need] -= 1
        prefix.append(target[i])
    else:
        # CLAUSE: handle_target_prefix_case
        if len(source) > len(target):
            candidate = "".join(prefix) + build_from_counts(counts)
            if best is None or candidate < best:
                best = candidate
    return best


# CLAUSE: emit_answer
def solve():
    source = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()
    print(smallest_greater_anagram(source, target) or "-1")


if __name__ == "__main__":
    solve()
''',
    "985C": r'''
import bisect
import sys


# CLAUSE: parse_barrel_input
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], sorted(data[3:])


# CLAUSE: identify_usable_staves
def usable_prefix(staves, limit):
    return bisect.bisect_right(staves, staves[0] + limit)


# CLAUSE: verify_enough_minima
def feasible(usable, barrels):
    return usable >= barrels


# CLAUSE: choose_next_minimum
def step_position(pos, k, usable, remaining_minima):
    return pos + min(k, usable - pos - remaining_minima)


# CLAUSE: accumulate_barrel_volume
def maximum_volume(n, k, usable, staves):
    total = 0
    pos = 0
    for barrel in range(n):
        total += staves[pos]
        pos = step_position(pos, k, usable, n - barrel - 1)
    return total


# CLAUSE: emit_answer
def solve():
    n, k, limit, staves = read_input()
    usable = usable_prefix(staves, limit)
    print(maximum_volume(n, k, usable, staves) if feasible(usable, n) else 0)


if __name__ == "__main__":
    solve()
''',
    "519C": r'''
import sys


# CLAUSE: parse_counts
def read_counts():
    return map(int, sys.stdin.buffer.read().split())


# CLAUSE: normalize_groups
def split_groups(a, b):
    return min(a, b), max(a, b)


# CLAUSE: compute_total_bound
def total_bound(a, b):
    return (a + b) // 3


# CLAUSE: compute_minority_bound
def minority_bound(a, b):
    return min(a, b)


# CLAUSE: select_maximum_teams
def max_teams(a, b):
    return min(total_bound(a, b), minority_bound(a, b))


# CLAUSE: emit_answer
def solve():
    a, b = read_counts()
    print(max_teams(a, b))


if __name__ == "__main__":
    solve()
''',
    "1715B": r'''
import sys


# CLAUSE: parse_test_cases
def read_ints():
    return list(map(int, sys.stdin.buffer.read().split()))


# CLAUSE: derive_sum_bounds
def bounds(n, k, b):
    base = b * k
    return base, base + n * (k - 1)


# CLAUSE: check_feasibility
def possible(n, k, b, s):
    low, high = bounds(n, k, b)
    return low <= s <= high


# CLAUSE: seed_beauty_value
def initial_array(n, k, b):
    arr = [0] * n
    arr[0] = b * k
    return arr


# CLAUSE: distribute_remainder
def construct(n, k, b, s):
    arr = initial_array(n, k, b)
    extra = s - b * k
    for i in range(n):
        add = min(extra, k - 1)
        arr[i] += add
        extra -= add
    return arr


# CLAUSE: emit_answers
def solve():
    data = read_ints()
    if not data:
        return
    pos = 1
    out = []
    for _ in range(data[0]):
        n, k, b, s = data[pos:pos + 4]
        pos += 4
        out.append("-1" if not possible(n, k, b, s) else " ".join(map(str, construct(n, k, b, s))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
''',
    "2051F": r'''
import sys


# CLAUSE: classify_cut_position
def classify(left, right, cut):
    if cut < left:
        return -1
    if cut > right:
        return 1
    return 0


# CLAUSE: shift_reachable_interval
def shifted_parts(left, right, cut, side):
    if side < 0:
        return [(left - 1, right)]
    if side > 0:
        return [(left, right + 1)]
    parts = []
    if left < cut:
        parts.append((left, cut))
    if cut < right:
        parts.append((cut, right))
    return parts


# CLAUSE: spawn_edge_positions
def edge_parts(side, n):
    return [(1, 1), (n, n)] if side == 0 else []


# CLAUSE: merge_intervals
def merge_intervals(intervals):
    intervals = sorted((l, r) for l, r in intervals if l <= r)
    merged = []
    for left, right in intervals:
        if not merged or left > merged[-1][1] + 1:
            merged.append([left, right])
        else:
            merged[-1][1] = max(merged[-1][1], right)
    return [(l, r) for l, r in merged]


# CLAUSE: process_operations
def solve_case(n, m, queries):
    intervals = [(m, m)]
    answers = []
    for cut in queries:
        nxt = []
        for left, right in intervals:
            side = classify(left, right, cut)
            nxt.extend(shifted_parts(left, right, cut, side))
            nxt.extend(edge_parts(side, n))
        intervals = merge_intervals(nxt)
        answers.append(str(sum(right - left + 1 for left, right in intervals)))
    return " ".join(answers)


# CLAUSE: parse_and_emit
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    pos = 1
    out = []
    for _ in range(data[0]):
        n, m, q = data[pos:pos + 3]
        pos += 3
        out.append(solve_case(n, m, data[pos:pos + q]))
        pos += q
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
''',
    "534B": r'''
import sys


# CLAUSE: parse_motion_parameters
def read_values():
    return tuple(map(int, sys.stdin.buffer.read().split()))


# CLAUSE: derive_start_cap
def start_cap(v1, d, second):
    return v1 + second * d


# CLAUSE: derive_finish_cap
def finish_cap(v2, d, t, second):
    return v2 + (t - 1 - second) * d


# CLAUSE: choose_speed_each_second
def speed_at(v1, v2, t, d, second):
    return min(start_cap(v1, d, second), finish_cap(v2, d, t, second))


# CLAUSE: accumulate_distance
def covered_distance(v1, v2, t, d):
    total = 0
    for second in range(t):
        total += speed_at(v1, v2, t, d, second)
    return total


# CLAUSE: emit_answer
def solve():
    v1, v2, t, d = read_values()
    print(covered_distance(v1, v2, t, d))


if __name__ == "__main__":
    solve()
''',
    "801B": r'''
import sys


# CLAUSE: parse_key_strings
def read_strings():
    data = sys.stdin.read().split()
    return data[0], data[1]


# CLAUSE: validate_position
def valid_pair(a, b):
    return b <= a


# CLAUSE: derive_forced_character
def forced_character(a, b):
    return b


# CLAUSE: construct_candidate
def make_candidate(x, y):
    out = []
    for a, b in zip(x, y):
        if not valid_pair(a, b):
            return "-1"
        out.append(forced_character(a, b))
    return "".join(out)


# CLAUSE: verify_length_alignment
def compatible_lengths(x, y):
    return len(x) == len(y)


# CLAUSE: emit_answer
def solve():
    x, y = read_strings()
    print(make_candidate(x, y) if compatible_lengths(x, y) else "-1")


if __name__ == "__main__":
    solve()
''',
    "1223D": r'''
import sys


# CLAUSE: record_value_spans
def occurrence_spans(values):
    first = {}
    last = {}
    for i, value in enumerate(values):
        if value not in first:
            first[value] = i
        last[value] = i
    return first, last


# CLAUSE: sort_distinct_values
def ordered_values(first):
    return sorted(first)


# CLAUSE: detect_compatible_neighbors
def compatible(prev, cur, first, last):
    return last[prev] < first[cur]


# CLAUSE: compute_longest_chain
def longest_chain(values, first, last):
    if not values:
        return 0
    best = cur = 1
    for i in range(1, len(values)):
        if compatible(values[i - 1], values[i], first, last):
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
    return best


# CLAUSE: derive_minimum_operations
def minimum_operations(values):
    first, last = occurrence_spans(values)
    order = ordered_values(first)
    return len(order) - longest_chain(order, first, last)


# CLAUSE: parse_and_emit
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    pos = 1
    out = []
    for _ in range(data[0]):
        n = data[pos]
        pos += 1
        out.append(str(minimum_operations(data[pos:pos + n])))
        pos += n
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
''',
}


def main() -> int:
    BACKUP.mkdir(parents=True, exist_ok=True)
    for problem in PROBLEMS:
        pdir = OUT / problem
        if not pdir.exists():
            raise SystemExit(f"missing problem dir: {pdir}")
        backup_dir = BACKUP / problem
        backup_dir.mkdir(parents=True, exist_ok=True)
        source = SOURCES[problem].strip() + "\n"
        for i in range(1, 6):
            dest = pdir / f"candidate_{i}.py"
            if dest.exists():
                shutil.copy2(dest, backup_dir / dest.name)
            dest.write_text(source)
    print(f"Repaired candidates for {len(PROBLEMS)} problems")
    print(f"Backup: {BACKUP.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
