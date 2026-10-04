# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def parse_input(nums):
    if not nums:
        return []
    parsed = []
    at = 1
    good = True
    for _ in range(nums[0]):
        if at >= len(nums):
            good = False
            break
        n = nums[at]
        at += 1
        end = at + 2 * n + 1
        if end > len(nums):
            good = False
            break
        parsed.append((n, nums[at:end]))
        at = end
    if good and at == len(nums):
        return parsed
    n = nums[0]
    expected = 2 * n + 1
    if len(nums) == expected + 1:
        return [(n, nums[1:])]
    return []

def solve_case(n, arr):
    buckets = [[] for _ in range(n + 1)]
    for position in range(1, len(arr) + 1):
        value = arr[position - 1]
        if 0 <= value <= n:
            buckets[value].append(position)
            if len(buckets[value]) == 3:
                return buckets[value]
    return []

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    output = []
    for n, arr in parse_input(nums):
        triple = solve_case(n, arr)
        if triple:
            output.append(" ".join(map(str, triple)))
    print("\n".join(output), end="")

if __name__ == "__main__":
    main()
