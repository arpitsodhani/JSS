import sys
from math import isqrt

LIMIT = 10 ** 18

# CLAUSE: enumerate_anchor_pairs
def enumerate_anchor_pairs(values):
    ordered = sorted(values)
    n = len(ordered)
    for left in range(n):
        ai = ordered[left]
        for right in range(left + 1, n):
            yield ai, ordered[right]

# CLAUSE: factor_pair_differences
def factor_pair_differences(diff):
    root = isqrt(diff)
    for u in range(1, root + 1):
        if diff % u == 0:
            v = diff // u
            if (u & 1) == (v & 1):
                yield u, v

# CLAUSE: derive_candidate_shift
def derive_candidate_shift(base, u, v):
    s = (v - u) // 2
    return s * s - base

# CLAUSE: validate_shift_bounds
def validate_shift_bounds(x):
    return 0 <= x <= LIMIT

# CLAUSE: count_square_hits
def count_square_hits(values, x):
    hits = 0
    for value in values:
        y = value + x
        r = isqrt(y)
        if r * r == y:
            hits += 1
    return hits

# CLAUSE: aggregate_best_squareness
def aggregate_best_squareness(values):
    best = 1
    used = set()
    for ai, aj in enumerate_anchor_pairs(values):
        for u, v in factor_pair_differences(aj - ai):
            x = derive_candidate_shift(ai, u, v)
            if validate_shift_bounds(x) and x not in used:
                used.add(x)
                best = max(best, count_square_hits(values, x))
    return best

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        out.append(str(aggregate_best_squareness(arr)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
