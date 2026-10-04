# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = list(map(int, sys.stdin.read().split()))
    bars = parts[1:]
    unique_lengths = set(bars)
    tallest = 0
    for length in unique_lengths:
        amount = bars.count(length)
        if amount > tallest:
            tallest = amount

# CLAUSE: finish_program
    print(tallest, len(unique_lengths))

if __name__ == "__main__":
    main()
