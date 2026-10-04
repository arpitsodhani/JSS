# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    counts = [0] * 4
    coords = iter(raw[1:])
    for xb, yb in zip(coords, coords):
        x = int(xb)
        y = int(yb)
        counts[(((x >> 1) & 1) << 1) + ((y >> 1) & 1)] += 1

    total = n * (n - 1) * (n - 2) // 6
    bad = 0
    prefix_pairs = 0
    seen = 0
    for amount in counts:
        bad += prefix_pairs * amount
        prefix_pairs += seen * amount
        seen += amount

    print(total - bad)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
