import sys
from math import isqrt

MAX_SHIFT = 10 ** 18

# CLAUSE: enumerate_anchor_pairs
def enumerate_anchor_pairs(a):
    a = sorted(a)
    pairs = []
    for j, high in enumerate(a):
        for low in a[:j]:
            pairs.append((low, high))
    return pairs

# CLAUSE: factor_pair_differences
def factor_pair_differences(d, cache):
    if d in cache:
        return cache[d]
    factors = []
    q = 1
    while q * q <= d:
        if d % q == 0:
            other = d // q
            if (q + other) % 2 == 0:
                factors.append((q, other))
        q += 1
    cache[d] = factors
    return factors

# CLAUSE: derive_candidate_shift
def derive_candidate_shift(a_i, pair):
    u, v = pair
    lower_root = (v - u) >> 1
    return lower_root * lower_root - a_i

# CLAUSE: validate_shift_bounds
def validate_shift_bounds(x):
    if x < 0:
        return False
    if x > MAX_SHIFT:
        return False
    return True

# CLAUSE: count_square_hits
def count_square_hits(a, x):
    total = 0
    for item in a:
        z = item + x
        root = isqrt(z)
        total += root * root == z
    return total

# CLAUSE: aggregate_best_squareness
def aggregate_best_squareness(a):
    answer = 1
    checked = set()
    factor_cache = {}
    for small, large in enumerate_anchor_pairs(a):
        choices = factor_pair_differences(large - small, factor_cache)
        for pair in choices:
            x = derive_candidate_shift(small, pair)
            if not validate_shift_bounds(x) or x in checked:
                continue
            checked.add(x)
            score = count_square_hits(a, x)
            if score > answer:
                answer = score
    return answer

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    idx = 1
    res = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        a = nums[idx:idx + n]
        idx += n
        res.append(str(aggregate_best_squareness(a)))
    sys.stdout.write("\n".join(res))

main()
