# CLAUSE: setup_environment
import sys
from math import sqrt

# CLAUSE: solve_logic
def main():
    data = list(map(float, sys.stdin.buffer.read().split()))
    pos = 0
    n = int(data[pos])
    pos += 1
    p = data[pos]
    q = data[pos + 1]
    m = int(data[pos + 2])
    pos += 3

    lines = []
    for _ in range(n):
        a = data[pos]
        b = data[pos + 1]
        lines.append((a, b, -(a * a + b * b)))
        pos += 2

    distances = []
    for i in range(n):
        a1, b1, c1 = lines[i]
        for j in range(i + 1, n):
            a2, b2, c2 = lines[j]
            det = a1 * b2 - a2 * b1
            if abs(det) > 1e-12:
                x = (b1 * c2 - b2 * c1) / det
                y = (a2 * c1 - a1 * c2) / det
                distances.append(sqrt((x - p) * (x - p) + (y - q) * (y - q)))

    distances.sort()
    print(f"{sum(distances[:m]):.9f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
