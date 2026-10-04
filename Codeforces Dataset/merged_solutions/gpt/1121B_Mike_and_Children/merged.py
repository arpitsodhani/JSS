import sys
from collections import defaultdict

# CLAUSE: enumerate_pair_sums
def enumerate_pair_sums(values):
    pairs = []
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((values[i] + values[j], i, j))
    return pairs

# CLAUSE: group_pairs_by_sum
def group_pairs_by_sum(pairs):
    groups = defaultdict(list)
    for total, i, j in pairs:
        groups[total].append((i, j))
    return groups

# CLAUSE: select_candidate_sum
def select_candidate_sum(groups):
    return groups.items()

# CLAUSE: track_used_sweets
def track_used_sweets(n):
    return [False] * n

# CLAUSE: count_disjoint_pairs
def count_disjoint_pairs(pairs, n):
    used = track_used_sweets(n)
    count = 0
    for i, j in pairs:
        if not used[i] and not used[j]:
            used[i] = True
            used[j] = True
            count += 1
    return count

# CLAUSE: maximize_children_count
def maximize_children_count(values):
    pairs = enumerate_pair_sums(values)
    groups = group_pairs_by_sum(pairs)
    best = 0
    for _, same_sum_pairs in select_candidate_sum(groups):
        best = max(best, count_disjoint_pairs(same_sum_pairs, len(values)))
    return best

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    values = data[1:1 + n]
    print(maximize_children_count(values))

if __name__ == "__main__":
    main()
