# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    count = items[0]
    ordered = sorted(items[1:])
    first_half = ordered[:count // 2]
    second_half = ordered[count // 2:][::-1]
    result = sum((x + y) ** 2 for x, y in zip(first_half, second_half))
    sys.stdout.write(f"{result}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
