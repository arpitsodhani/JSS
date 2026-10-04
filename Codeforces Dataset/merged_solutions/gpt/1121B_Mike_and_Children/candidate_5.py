import sys

# CLAUSE: enumerate_pair_sums
def enumerate_pair_sums(a):
    n = len(a)
    sums = []
    pairs = []
    for i in range(n - 1):
        ai = a[i]
        for j in range(i + 1, n):
            sums.append(ai + a[j])
            pairs.append((i, j))
    return sums, pairs

# CLAUSE: group_pairs_by_sum
def group_pairs_by_sum(sums, pairs):
    groups = {}
    for idx in range(len(sums)):
        groups.setdefault(sums[idx], []).append(idx)
    return groups, pairs

# CLAUSE: select_candidate_sum
def select_candidate_sum(groups):
    return list(groups.values())

# CLAUSE: track_used_sweets
def track_used_sweets(n):
    return [0 for _ in range(n)]

# CLAUSE: count_disjoint_pairs
def count_disjoint_pairs(indices, pairs, n):
    used = track_used_sweets(n)
    children = 0
    for idx in indices:
        i, j = pairs[idx]
        if used[i] or used[j]:
            continue
        used[i] = 1
        used[j] = 1
        children += 1
    return children

# CLAUSE: maximize_children_count
def maximize_children_count(a):
    sums, pairs = enumerate_pair_sums(a)
    groups, pairs = group_pairs_by_sum(sums, pairs)
    best = 0
    for indices in select_candidate_sum(groups):
        children = count_disjoint_pairs(indices, pairs, len(a))
        if children > best:
            best = children
    return best

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = [int(data[i]) for i in range(1, n + 1)]
    print(maximize_children_count(a))

if __name__ == "__main__":
    main()
