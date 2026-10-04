import sys

def bounds(n, k, b):
    # CLAUSE: derive_beauty_bounds
    minimum = k * b
    maximum = minimum + (k - 1) * n
    return minimum, maximum

def construct(n, k, b, s):
    minimum, maximum = bounds(n, k, b)

    # CLAUSE: validate_sum_feasibility
    possible = minimum <= s <= maximum
    if not possible:
        return []

    # CLAUSE: reserve_beauty_core
    result = [minimum] + [0 for _ in range(n - 1)]

    # CLAUSE: allocate_remainder_budget
    extra = s - minimum

    # CLAUSE: distribute_surplus_across_slots
    idx = n - 1
    while extra:
        portion = k - 1 if extra >= k - 1 else extra
        result[idx] += portion
        extra -= portion
        idx -= 1

    # CLAUSE: preserve_floor_contributions
    valid = all(x % k < k for x in result) and sum(x // k for x in result) == b
    if not valid:
        return []

    # CLAUSE: emit_constructed_array
    return result

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    lines = []
    at = 1
    for _ in range(t):
        n = nums[at]
        k = nums[at + 1]
        b = nums[at + 2]
        s = nums[at + 3]
        at += 4
        arr = construct(n, k, b, s)
        lines.append(" ".join(map(str, arr)) if arr else "-1")
    print("\n".join(lines))

main()
