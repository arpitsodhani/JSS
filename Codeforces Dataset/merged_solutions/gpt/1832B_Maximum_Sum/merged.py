# CLAUSE: sort_values
import sys

def sort_values(values):
    return sorted(values)

# CLAUSE: compute_removed_pair_prefixes
def compute_removed_pair_prefixes(values):
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    return prefix

# CLAUSE: compute_removed_max_suffixes
def compute_removed_max_suffixes(values):
    suffix = [0] * (len(values) + 1)
    for i in range(len(values) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + values[i]
    return suffix

# CLAUSE: enumerate_operation_split
def enumerate_operation_split(k):
    return range(k + 1)

# CLAUSE: evaluate_remaining_sum
def evaluate_remaining_sum(total, prefix, suffix, n, small_ops, k):
    removed_small = prefix[2 * small_ops]
    removed_large = suffix[n - (k - small_ops)]
    return total - removed_small - removed_large

# CLAUSE: maximize_survivor_sum
def maximize_survivor_sum(n, k, values):
    values = sort_values(values)
    prefix = compute_removed_pair_prefixes(values)
    suffix = compute_removed_max_suffixes(values)
    total = prefix[n]
    best = -1
    for small_ops in enumerate_operation_split(k):
        best = max(best, evaluate_remaining_sum(total, prefix, suffix, n, small_ops, k))
    return best

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
pos = 1
answers = []
for _ in range(t):
    n, k = data[pos], data[pos + 1]
    pos += 2
    arr = data[pos:pos + n]
    pos += n
    answers.append(str(maximize_survivor_sum(n, k, arr)))
sys.stdout.write("\n".join(answers))
