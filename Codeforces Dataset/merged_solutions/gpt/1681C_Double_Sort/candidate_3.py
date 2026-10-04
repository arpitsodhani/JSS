# CLAUSE: pair_positions
import sys
from collections import defaultdict

def pair_positions(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

# CLAUSE: construct_target_order
def construct_target_order(pairs):
    ordered = list(pairs)
    ordered.sort()
    return ordered

# CLAUSE: validate_dual_monotonicity
def validate_dual_monotonicity(target):
    return all(target[i][1] <= target[i + 1][1] for i in range(len(target) - 1))

# CLAUSE: locate_next_target_pair
def locate_next_target_pair(position_sets, current, start, needed):
    candidates = position_sets[needed]
    while start not in candidates and candidates:
        j = min(candidates)
        if j >= start and current[j] == needed:
            return j
        candidates.discard(j)
    if start in candidates and current[start] == needed:
        return start
    return -1

# CLAUSE: apply_synchronized_swap
def apply_synchronized_swap(position_sets, current, ops, i, j):
    if i == j:
        return
    left = current[i]
    right = current[j]
    position_sets[left].remove(i)
    position_sets[right].remove(j)
    current[i], current[j] = current[j], current[i]
    position_sets[left].add(j)
    position_sets[right].add(i)
    ops.append((i + 1, j + 1))

# CLAUSE: emit_operation_sequence
def solve_one(n, a, b):
    current = pair_positions(a, b)
    target = construct_target_order(current)
    if not validate_dual_monotonicity(target):
        return ["-1"]

    position_sets = defaultdict(set)
    for i, pair in enumerate(current):
        position_sets[pair].add(i)

    ops = []
    for i in range(n):
        j = locate_next_target_pair(position_sets, current, i, target[i])
        if j == -1:
            return ["-1"]
        apply_synchronized_swap(position_sets, current, ops, i, j)

    if len(ops) > 10000:
        return ["-1"]
    result = [str(len(ops))]
    result += [f"{i} {j}" for i, j in ops]
    return result

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 1
    answer = []
    for _ in range(nums[0]):
        n = nums[ptr]
        ptr += 1
        a = nums[ptr:ptr + n]
        ptr += n
        b = nums[ptr:ptr + n]
        ptr += n
        answer.extend(solve_one(n, a, b))
    sys.stdout.write("\n".join(answer))

main()
