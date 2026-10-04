# CLAUSE: setup_environment
import sys
from math import sqrt

# CLAUSE: solve_logic
def main():
    tokens = list(map(float, sys.stdin.buffer.read().split()))
    n = int(tokens[0])
    px, py = tokens[1], tokens[2]
    limit = int(tokens[3])

    a_vals = []
    b_vals = []
    c_vals = []
    index = 4
    for _ in range(n):
        a = tokens[index]
        b = tokens[index + 1]
        a_vals.append(a)
        b_vals.append(b)
        c_vals.append(-(a * a + b * b))
        index += 2

    result = []
    for i, (a1, b1, c1) in enumerate(zip(a_vals, b_vals, c_vals)):
        j = i + 1
        while j < n:
            a2 = a_vals[j]
            b2 = b_vals[j]
            c2 = c_vals[j]
            det = a1 * b2 - a2 * b1
            if abs(det) > 1e-12:
                x = (b1 * c2 - b2 * c1) / det
                y = (a2 * c1 - a1 * c2) / det
                dx = x - px
                dy = y - py
                result.append(sqrt(dx * dx + dy * dy))
            j += 1

    result.sort()
    total = 0.0
    for value in result[:limit]:
        total += value
    print("{:.9f}".format(total))

# CLAUSE: finish_program
main()
