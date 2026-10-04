import sys
from collections import defaultdict

# CLAUSE: enumerate_pair_sums
def enumerate_pair_sums(sweets):
    n = len(sweets)
    pairs = defaultdict(list)
    for i, first in enumerate(sweets):
        for j in range(i + 1, n):
            pairs[first + sweets[j]].append((i, j))
    return pairs

# CLAUSE: group_pairs_by_sum
def group_pairs_by_sum(pair_map):
    return [pair_map[key] for key in pair_map]

# CLAUSE: select_candidate_sum
def select_candidate_sum(groups):
    index = 0
    while index < len(groups):
        yield groups[index]
        index += 1

# CLAUSE: track_used_sweets
def track_used_sweets(n):
    return [-1] * n

# CLAUSE: count_disjoint_pairs
def count_disjoint_pairs(group, n):
    used = track_used_sweets(n)
    matched = 0
    for i, j in group:
        if used[i] < 0 and used[j] < 0:
            used[i] = matched
            used[j] = matched
            matched += 1
    return matched

# CLAUSE: maximize_children_count
def maximize_children_count(sweets):
    pair_map = enumerate_pair_sums(sweets)
    groups = group_pairs_by_sum(pair_map)
    result = 0
    for group in select_candidate_sum(groups):
        result = max(result, count_disjoint_pairs(group, len(sweets)))
    return result

raw = list(map(int, sys.stdin.buffer.read().split()))
print(maximize_children_count(raw[1:1 + raw[0]]))
