import sys

# CLAUSE: enumerate_pair_sums
def enumerate_pair_sums(arr):
    n = len(arr)
    pairs = []
    for right in range(1, n):
        for left in range(right):
            pairs.append((arr[left] + arr[right], left, right))
    return pairs

# CLAUSE: group_pairs_by_sum
def group_pairs_by_sum(pairs):
    groups = {}
    for total, left, right in pairs:
        if total not in groups:
            groups[total] = []
        groups[total].append((left, right))
    return groups

# CLAUSE: select_candidate_sum
def select_candidate_sum(groups):
    for total in groups:
        yield groups[total]

# CLAUSE: track_used_sweets
def track_used_sweets(n):
    return set()

# CLAUSE: count_disjoint_pairs
def count_disjoint_pairs(pairs, n):
    used = track_used_sweets(n)
    chosen = 0
    for left, right in pairs:
        if left not in used and right not in used:
            used.add(left)
            used.add(right)
            chosen += 1
    return chosen

# CLAUSE: maximize_children_count
def maximize_children_count(arr):
    pairs = enumerate_pair_sums(arr)
    groups = group_pairs_by_sum(pairs)
    maximum = 0
    for pairs_for_sum in select_candidate_sum(groups):
        value = count_disjoint_pairs(pairs_for_sum, len(arr))
        maximum = value if value > maximum else maximum
    return maximum

def main():
    data = sys.stdin.readline
    n = int(data())
    arr = list(map(int, data().split()))
    print(maximize_children_count(arr))

main()
