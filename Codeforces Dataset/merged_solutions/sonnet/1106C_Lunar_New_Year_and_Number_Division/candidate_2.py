# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    nums = values[1:]
    nums.sort()
    ans = 0
    for i in range(n // 2):
        total = nums[i] + nums[n - 1 - i]
        ans += total * total
    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
