# CLAUSE: sort_values
import sys

def sort_values(a):
    return sorted(a)

# CLAUSE: compute_removed_pair_prefixes
def compute_removed_pair_prefixes(a):
    prefix = [0] * (len(a) + 1)
    for i, x in enumerate(a, 1):
        prefix[i] = prefix[i - 1] + x
    return prefix

# CLAUSE: compute_removed_max_suffixes
def compute_removed_max_suffixes(a):
    prefix = compute_removed_pair_prefixes(a)
    total = prefix[-1]
    return prefix, total

# CLAUSE: enumerate_operation_split
def enumerate_operation_split(k):
    x = 0
    while x <= k:
        yield x
        x += 1

# CLAUSE: evaluate_remaining_sum
def evaluate_remaining_sum(prefix, total, n, k, x):
    left_removed_until = 2 * x
    right_remaining_until = n - (k - x)
    removed_small = prefix[left_removed_until]
    removed_large = total - prefix[right_remaining_until]
    return total - removed_small - removed_large

# CLAUSE: maximize_survivor_sum
def maximize_survivor_sum(n, k, a):
    a = sort_values(a)
    prefix, total = compute_removed_max_suffixes(a)
    best = -10**30
    for x in enumerate_operation_split(k):
        remaining = evaluate_remaining_sum(prefix, total, n, k, x)
        if remaining > best:
            best = remaining
    return best

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
p = 1
ans = []
for _ in range(t):
    n = data[p]
    k = data[p + 1]
    p += 2
    ans.append(str(maximize_survivor_sum(n, k, data[p:p + n])))
    p += n
sys.stdout.write("\n".join(ans))
