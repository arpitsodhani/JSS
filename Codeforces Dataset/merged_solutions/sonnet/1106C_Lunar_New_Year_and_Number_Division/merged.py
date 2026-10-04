# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


