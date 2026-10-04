# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    bars = sorted(nums[1:1 + n])
    best = 0
    different = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and bars[j] == bars[i]:
            j += 1
        count = j - i
        if count > best:
            best = count
        different += 1
        i = j

# CLAUSE: finish_program
    print(best, different)

if __name__ == "__main__":
    main()
