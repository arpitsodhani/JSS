# CLAUSE: setup_environment
import sys
from math import hypot

# CLAUSE: solve_logic
def read_case():
    parts = sys.stdin.buffer.read().split()
    n = int(parts[0])
    px = float(parts[1])
    py = float(parts[2])
    m = int(parts[3])
    pairs = []
    at = 4
    for _ in range(n):
        a = float(parts[at])
        b = float(parts[at + 1])
        pairs.append((a, b))
        at += 2
    return n, px, py, m, pairs

def main():
    n, px, py, m, pairs = read_case()
    prepared = [(a, b, -a * a - b * b) for a, b in pairs]
    found = []

    for i in range(n):
        a1, b1, c1 = prepared[i]
        for j in range(i + 1, n):
            a2, b2, c2 = prepared[j]
            denominator = a1 * b2 - a2 * b1
            if denominator < -1e-12 or denominator > 1e-12:
                ix = (b1 * c2 - b2 * c1) / denominator
                iy = (a2 * c1 - a1 * c2) / denominator
                found.append(hypot(ix - px, iy - py))

    found.sort()
    sys.stdout.write(f"{sum(found[0:m]):.9f}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
