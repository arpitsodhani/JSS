# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.read().split()))
    if not values:
        return
    counts = {}
    pairs = 0
    for length in values[1:values[0] + 1]:
        current = counts.get(length, 0) + 1
        if current == 2:
            pairs += 1
            current = 0
        counts[length] = current

# CLAUSE: finish_program
    sys.stdout.write(f"{pairs // 2}\n")

if __name__ == "__main__":
    main()
