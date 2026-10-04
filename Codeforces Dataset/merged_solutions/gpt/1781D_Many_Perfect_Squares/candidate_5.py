import sys
from math import isqrt

CAP = 10 ** 18

# CLAUSE: enumerate_anchor_pairs
def enumerate_anchor_pairs(values):
    ordered = sorted(values)
    for i, ai in enumerate(ordered):
        for aj in ordered[i + 1:]:
            yield (ai, aj)

# CLAUSE: factor_pair_differences
def factor_pair_differences(d):
    result = []
    top = isqrt(d)
    u = 1
    while u <= top:
        if d % u == 0:
            v = d // u
            if not ((u - v) & 1):
                result.append((u, v))
        u += 1
    return result

# CLAUSE: derive_candidate_shift
def derive_candidate_shift(a_i, u, v):
    smaller_root = (v - u) // 2
    return smaller_root * smaller_root - a_i

# CLAUSE: validate_shift_bounds
def validate_shift_bounds(x):
    return x in range(0, CAP + 1)

# CLAUSE: count_square_hits
def count_square_hits(values, x):
    cnt = 0
    for value in values:
        shifted = value + x
        r = isqrt(shifted)
        if r * r == shifted:
            cnt += 1
    return cnt

# CLAUSE: aggregate_best_squareness
def aggregate_best_squareness(values):
    ans = 1
    processed = set()
    for ai, aj in enumerate_anchor_pairs(values):
        diff = aj - ai
        for u, v in factor_pair_differences(diff):
            x = derive_candidate_shift(ai, u, v)
            if validate_shift_bounds(x):
                if x in processed:
                    continue
                processed.add(x)
                hits = count_square_hits(values, x)
                ans = hits if hits > ans else ans
    return ans

def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    t = data[0]
    k = 1
    answers = []
    for _ in range(t):
        n = data[k]
        k += 1
        arr = data[k:k + n]
        k += n
        answers.append(str(aggregate_best_squareness(arr)))
    print("\n".join(answers))

main()
