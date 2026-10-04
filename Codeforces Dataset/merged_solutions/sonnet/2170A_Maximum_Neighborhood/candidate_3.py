# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def value(n, r, c):
    return (r - 1) * n + c

def cost(n, r, c):
    total = value(n, r, c)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr = r + dr
        nc = c + dc
        if 1 <= nr <= n and 1 <= nc <= n:
            total += value(n, nr, nc)
    return total

def main():
    text = sys.stdin.read().strip()
    if not text:
        return
    n = int(text)
    cells = [(n, n)]
    if n >= 2:
        cells.append((n, n - 1))
    if n >= 3:
        cells.append((n - 1, n - 1))
    print(max(cost(n, r, c) for r, c in cells))

# CLAUSE: finish_program
main()
