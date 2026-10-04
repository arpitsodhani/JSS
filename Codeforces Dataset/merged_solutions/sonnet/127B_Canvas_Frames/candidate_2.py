# CLAUSE: setup_environment
import sys
from collections import Counter

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    counts = Counter(nums[1:n + 1])
    pair_count = sum(value // 2 for value in counts.values())

# CLAUSE: finish_program
    sys.stdout.write(str(pair_count // 2))

if __name__ == "__main__":
    main()
