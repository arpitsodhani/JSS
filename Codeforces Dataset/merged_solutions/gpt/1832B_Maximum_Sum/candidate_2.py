# CLAUSE: sort_values
import sys
from itertools import accumulate

def sort_values(a):
    a.sort()
    return a

# CLAUSE: compute_removed_pair_prefixes
def compute_removed_pair_prefixes(a):
    return [0] + list(accumulate(a))

# CLAUSE: compute_removed_max_suffixes
def compute_removed_max_suffixes(a):
    n = len(a)
    removed = [0] * (n + 1)
    running = 0
    for take in range(1, n + 1):
        running += a[n - take]
        removed[take] = running
    return removed

# CLAUSE: enumerate_operation_split
def enumerate_operation_split(k):
    splits = []
    for pairs in range(k + 1):
        splits.append((pairs, k - pairs))
    return splits

# CLAUSE: evaluate_remaining_sum
def evaluate_remaining_sum(total, pair_prefix, max_suffix, pairs, singles):
    return total - pair_prefix[pairs * 2] - max_suffix[singles]

# CLAUSE: maximize_survivor_sum
def maximize_survivor_sum(n, k, a):
    sorted_a = sort_values(a)
    pair_prefix = compute_removed_pair_prefixes(sorted_a)
    max_suffix = compute_removed_max_suffixes(sorted_a)
    total = pair_prefix[-1]
    answer = 0
    for pairs, singles in enumerate_operation_split(k):
        current = evaluate_remaining_sum(total, pair_prefix, max_suffix, pairs, singles)
        if current > answer:
            answer = current
    return answer

tokens = list(map(int, sys.stdin.buffer.read().split()))
cases = tokens[0]
idx = 1
out = []
for _ in range(cases):
    n = tokens[idx]
    k = tokens[idx + 1]
    idx += 2
    out.append(str(maximize_survivor_sum(n, k, tokens[idx:idx + n])))
    idx += n
print("\n".join(out))
