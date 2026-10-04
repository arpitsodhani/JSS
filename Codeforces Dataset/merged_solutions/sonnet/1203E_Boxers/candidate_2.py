# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    arr = nums[1:n + 1]
    arr.sort()
    chosen = set()
    for weight in arr:
        for candidate in (weight - 1, weight, weight + 1):
            if candidate > 0 and candidate not in chosen:
                chosen.add(candidate)
                break
    sys.stdout.write(str(len(chosen)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
