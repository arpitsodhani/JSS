import sys
from math import isqrt

BOUND = 1000000000000000000

# CLAUSE: enumerate_anchor_pairs
def enumerate_anchor_pairs(nums):
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        first = nums[i]
        for j in range(i + 1, len(nums)):
            yield first, nums[j], nums[j] - first

# CLAUSE: factor_pair_differences
def factor_pair_differences(d):
    u = 1
    while u <= d // u:
        if d % u == 0:
            v = d // u
            if u % 2 == v % 2:
                yield u, v
        u += 1

# CLAUSE: derive_candidate_shift
def derive_candidate_shift(a_i, u, v):
    s = (v - u) // 2
    square = s ** 2
    return square - a_i

# CLAUSE: validate_shift_bounds
def validate_shift_bounds(x):
    return x >= 0 and x <= BOUND

# CLAUSE: count_square_hits
def count_square_hits(nums, x):
    return sum(1 for z in (value + x for value in nums) if isqrt(z) ** 2 == z)

# CLAUSE: aggregate_best_squareness
def aggregate_best_squareness(nums):
    candidates = set()
    for a_i, _, d in enumerate_anchor_pairs(nums):
        for u, v in factor_pair_differences(d):
            x = derive_candidate_shift(a_i, u, v)
            if validate_shift_bounds(x):
                candidates.add(x)
    ans = 1
    for x in candidates:
        ans = max(ans, count_square_hits(nums, x))
    return ans

def main():
    stream = list(map(int, sys.stdin.buffer.read().split()))
    t = stream[0]
    p = 1
    answers = []
    for _ in range(t):
        n = stream[p]
        p += 1
        nums = stream[p:p + n]
        p += n
        answers.append(str(aggregate_best_squareness(nums)))
    print("\n".join(answers))

main()
