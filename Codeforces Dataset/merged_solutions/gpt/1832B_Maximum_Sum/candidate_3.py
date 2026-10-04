# CLAUSE: sort_values
import sys

def sort_values(numbers):
    return sorted(numbers)

# CLAUSE: compute_removed_pair_prefixes
def compute_removed_pair_prefixes(numbers, k):
    removed = [0] * (k + 1)
    cursor = 0
    for used_pairs in range(1, k + 1):
        cursor += numbers[2 * used_pairs - 2] + numbers[2 * used_pairs - 1]
        removed[used_pairs] = cursor
    return removed

# CLAUSE: compute_removed_max_suffixes
def compute_removed_max_suffixes(numbers, k):
    removed = [0] * (k + 1)
    cursor = 0
    for used_max in range(1, k + 1):
        cursor += numbers[-used_max]
        removed[used_max] = cursor
    return removed

# CLAUSE: enumerate_operation_split
def enumerate_operation_split(k):
    for left_deletions in range(k + 1):
        yield left_deletions

# CLAUSE: evaluate_remaining_sum
def evaluate_remaining_sum(total, small_removed, large_removed, left_deletions, k):
    right_deletions = k - left_deletions
    return total - small_removed[left_deletions] - large_removed[right_deletions]

# CLAUSE: maximize_survivor_sum
def maximize_survivor_sum(n, k, numbers):
    ordered = sort_values(numbers)
    small_removed = compute_removed_pair_prefixes(ordered, k)
    large_removed = compute_removed_max_suffixes(ordered, k)
    total = sum(ordered)
    best = None
    for left_deletions in enumerate_operation_split(k):
        score = evaluate_remaining_sum(total, small_removed, large_removed, left_deletions, k)
        if best is None or score > best:
            best = score
    return best

raw = sys.stdin.buffer.read().split()
t = int(raw[0])
at = 1
res = []
for _ in range(t):
    n = int(raw[at])
    k = int(raw[at + 1])
    at += 2
    values = [int(x) for x in raw[at:at + n]]
    at += n
    res.append(str(maximize_survivor_sum(n, k, values)))
sys.stdout.write("\n".join(res))
