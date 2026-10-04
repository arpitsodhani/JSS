# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    best = None
    ans = 1
    for i, people in enumerate(nums[1:1 + n]):
        wait = i if people <= i else i + ((people - i + n - 1) // n) * n
        if best is None or wait < best:
            best = wait
            ans = i + 1
    sys.stdout.write(str(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
