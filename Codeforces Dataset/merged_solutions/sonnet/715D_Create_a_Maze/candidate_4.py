# CLAUSE: setup_environment
import sys
from math import comb

# CLAUSE: solve_logic
def main():
    target = int(sys.stdin.readline())
    rows = cols = 32
    horizontal = [[False] * cols for _ in range(rows + 1)]
    vertical = [[False] * (cols + 1) for _ in range(rows)]

    for c in range(1, cols):
        horizontal[1][c] = True

    for r in range(2, rows + 1):
        for c in range(1, cols):
            horizontal[r][c] = True

    for r in range(1, rows):
        for c in range(2, cols):
            vertical[r][c] = True

    for total in range(60, -1, -1):
        best = 0
        best_take = None
        first = max(0, total - 30)
        last = min(30, total)
        for take in range(first, last + 1):
            current = comb(total, take)
            if best < current <= target:
                best = current
                best_take = take
        if best_take is not None:
            r = best_take + 2
            c = total - best_take + 2
            if c < cols:
                horizontal[r][c] = True
            target -= best
            if target == 0:
                break

    locked = []
    for r in range(1, rows + 1):
        for c in range(1, cols):
            if not horizontal[r][c]:
                locked.append((r, c, r, c + 1))

    for r in range(1, rows):
        for c in range(1, cols + 1):
            if not vertical[r][c]:
                locked.append((r, c, r + 1, c))

    answer = ["%d %d" % (rows, cols), str(len(locked))]
    answer += ["%d %d %d %d" % edge for edge in locked]
    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
