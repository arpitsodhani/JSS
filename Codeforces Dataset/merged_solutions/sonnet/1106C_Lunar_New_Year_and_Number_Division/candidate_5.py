# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def compute(numbers):
    numbers.sort()
    total = 0
    for left, right in zip(numbers, reversed(numbers)):
        if left > right:
            break
        pair_sum = left + right
        total += pair_sum * pair_sum
    return total

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    nums = raw[1:]
    sys.stdout.write(str(compute(nums)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
