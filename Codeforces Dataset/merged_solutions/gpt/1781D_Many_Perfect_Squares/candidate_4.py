import sys
from math import isqrt

LIMIT_X = 10 ** 18

# CLAUSE: enumerate_anchor_pairs
def enumerate_anchor_pairs(a):
    b = sorted(a)
    n = len(b)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            yield b[i], b[j]
            j += 1
        i += 1

# CLAUSE: factor_pair_differences
def factor_pair_differences(d):
    divisors = []
    for u in range(1, isqrt(d) + 1):
        if d % u:
            continue
        v = d // u
        if (u ^ v) & 1:
            continue
        divisors.append((u, v))
    return divisors

# CLAUSE: derive_candidate_shift
def derive_candidate_shift(a_i, u, v):
    low = (v - u) // 2
    x = low * low
    x -= a_i
    return x

# CLAUSE: validate_shift_bounds
def validate_shift_bounds(x):
    return 0 <= x <= LIMIT_X

# CLAUSE: count_square_hits
def count_square_hits(a, x):
    hits = 0
    for value in a:
        candidate = value + x
        root = isqrt(candidate)
        if candidate == root * root:
            hits += 1
    return hits

# CLAUSE: aggregate_best_squareness
def aggregate_best_squareness(a):
    ans = 1
    seen = {}
    for left, right in enumerate_anchor_pairs(a):
        for u, v in factor_pair_differences(right - left):
            x = derive_candidate_shift(left, u, v)
            if validate_shift_bounds(x):
                seen[x] = None
    for x in seen:
        current = count_square_hits(a, x)
        if current > ans:
            ans = current
    return ans

def main():
    data = sys.stdin.buffer.read().split()
    tests = int(data[0])
    at = 1
    result = []
    for _ in range(tests):
        n = int(data[at])
        at += 1
        a = [int(x) for x in data[at:at + n]]
        at += n
        result.append(str(aggregate_best_squareness(a)))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
