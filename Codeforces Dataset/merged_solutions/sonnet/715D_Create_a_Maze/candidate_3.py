# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def choose_cells(x):
    cells = []
    for total in range(60, -1, -1):
        low = 0 if total <= 30 else total - 30
        high = total if total < 30 else 30
        best_value = -1
        best_row = -1
        for row in range(low, high + 1):
            value = math.comb(total, row)
            if best_value < value <= x:
                best_value = value
                best_row = row
        if best_row >= 0:
            cells.append((best_row + 2, total - best_row + 2))
            x -= best_value
            if x == 0:
                return cells
    return cells

def main():
    x = int(sys.stdin.readline())
    n, m = 32, 32
    opened = set()

    for col in range(1, m):
        opened.add((1, col, 1, col + 1))

    for row in range(2, n + 1):
        for col in range(1, m):
            opened.add((row, col, row, col + 1))

    for row in range(1, n):
        for col in range(2, m):
            opened.add((row, col, row + 1, col))

    for row, col in choose_cells(x):
        opened.add((row, col, row, col + 1))

    locked = []
    for row in range(1, n + 1):
        for col in range(1, m):
            if (row, col, row, col + 1) not in opened:
                locked.append((row, col, row, col + 1))

    for row in range(1, n):
        for col in range(1, m + 1):
            if (row, col, row + 1, col) not in opened:
                locked.append((row, col, row + 1, col))

    lines = ["32 32", str(len(locked))]
    for item in locked:
        lines.append("%d %d %d %d" % item)
    print("\n".join(lines))

# CLAUSE: finish_program
main()
