# CLAUSE: setup_environment
import sys
from math import comb

# CLAUSE: solve_logic
def selected_taps(value):
    result = []
    totals = list(range(61))
    totals.reverse()
    for total in totals:
        candidates = []
        start = max(0, total - 30)
        stop = min(30, total)
        for left in range(start, stop + 1):
            ways = comb(total, left)
            if ways <= value:
                candidates.append((ways, left))
        if candidates:
            ways, left = max(candidates)
            result.append((left + 2, total - left + 2))
            value -= ways
        if value == 0:
            break
    return result

def main():
    x = int(sys.stdin.readline())
    n = 32
    m = 32
    free = {}

    for r in range(1, n + 1):
        free[(r, 1, r, 2)] = r >= 1
        for c in range(2, m):
            free[(r, c, r, c + 1)] = True

    for r in range(1, n):
        free[(r, 1, r + 1, 1)] = False
        for c in range(2, m):
            free[(r, c, r + 1, c)] = True
        free[(r, m, r + 1, m)] = False

    for r, c in selected_taps(x):
        if c < m:
            free[(r, c, r, c + 1)] = True

    locks = []
    for edge, is_open in free.items():
        if not is_open:
            locks.append(edge)

    lines = []
    lines.append(str(n) + " " + str(m))
    lines.append(str(len(locks)))
    for a, b, c, d in locks:
        lines.append(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
main()
