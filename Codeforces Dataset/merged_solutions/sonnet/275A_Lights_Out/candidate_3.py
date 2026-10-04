# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def toggles_from(presses, row, col):
    total = presses[row][col]
    if row:
        total += presses[row - 1][col]
    if row + 1 < 3:
        total += presses[row + 1][col]
    if col:
        total += presses[row][col - 1]
    if col + 1 < 3:
        total += presses[row][col + 1]
    return total

def main():
    nums = list(map(int, sys.stdin.read().split()))
    presses = [nums[i:i + 3] for i in range(0, 9, 3)]
    rows = []

    for r in range(3):
        row = []
        for c in range(3):
            row.append(str(1 - toggles_from(presses, r, c) % 2))
        rows.append("".join(row))

    print("\n".join(rows))

# CLAUSE: finish_program
main()
