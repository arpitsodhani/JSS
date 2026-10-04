# CLAUSE: sort_values
import sys

def sort_values(items):
    items = list(items)
    items.sort()
    return items

# CLAUSE: compute_removed_pair_prefixes
def compute_removed_pair_prefixes(items, k):
    sums = [0]
    removed = 0
    for end in range(2, 2 * k + 1, 2):
        removed += items[end - 2] + items[end - 1]
        sums.append(removed)
    return sums

# CLAUSE: compute_removed_max_suffixes
def compute_removed_max_suffixes(items, k):
    sums = [0]
    removed = 0
    n = len(items)
    for i in range(k):
        removed += items[n - 1 - i]
        sums.append(removed)
    return sums

# CLAUSE: enumerate_operation_split
def enumerate_operation_split(k):
    return [(two_min_ops, k - two_min_ops) for two_min_ops in range(k + 1)]

# CLAUSE: evaluate_remaining_sum
def evaluate_remaining_sum(total_sum, two_min_removed, max_removed, split):
    two_min_ops, max_ops = split
    return total_sum - two_min_removed[two_min_ops] - max_removed[max_ops]

# CLAUSE: maximize_survivor_sum
def maximize_survivor_sum(n, k, items):
    items = sort_values(items)
    two_min_removed = compute_removed_pair_prefixes(items, k)
    max_removed = compute_removed_max_suffixes(items, k)
    total_sum = sum(items)
    candidates = []
    for split in enumerate_operation_split(k):
        candidates.append(evaluate_remaining_sum(total_sum, two_min_removed, max_removed, split))
    return max(candidates)

values = list(map(int, sys.stdin.buffer.read().split()))
t = values[0]
offset = 1
lines = []
for _ in range(t):
    n, k = values[offset], values[offset + 1]
    offset += 2
    lines.append(str(maximize_survivor_sum(n, k, values[offset:offset + n])))
    offset += n
sys.stdout.write("\n".join(lines))
