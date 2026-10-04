# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import comb

def main():
    x = int(sys.stdin.readline())
    
    n = 32
    m = 32
    
    open_edges = set()
    
    def add_edge(a, b, c, d):
        if abs(a - c) + abs(b - d) == 1:
            open_edges.add((a, b, c, d))
            open_edges.add((c, d, a, b))
    
    # A direct corridor from (1, 1) to the top row.
    for j in range(1, m):
        add_edge(1, j, 1, j + 1)
    
    # Pascal triangle area: ways to (i, j) are C(i + j - 4, i - 2).
    for i in range(2, n + 1):
        for j in range(1, m):
            add_edge(i, j, i, j + 1)
    for i in range(1, n):
        for j in range(2, m):
            add_edge(i, j, i + 1, j)
    
    # Collect x as a sum of binomial coefficients from the last column.
    need = x
    taps = []
    for s in range(60, -1, -1):
        best = None
        for r in range(0, min(30, s) + 1):
            if s - r <= 30:
                value = comb(s, r)
                if value <= need and (best is None or value > best[0]):
                    best = (value, r)
        if best is not None:
            value, r = best
            taps.append((r + 2, s - r + 2))
            need -= value
        if need == 0:
            break
    
    # Route selected cells to the finish through the last column.
    for i, j in taps:
        add_edge(i, j, i, j + 1)
    
    locks = []
    for i in range(1, n + 1):
        for j in range(1, m):
            if (i, j, i, j + 1) not in open_edges:
                locks.append((i, j, i, j + 1))
    for i in range(1, n):
        for j in range(1, m + 1):
            if (i, j, i + 1, j) not in open_edges:
                locks.append((i, j, i + 1, j))
    
    print(n, m)
    print(len(locks))
    for edge in locks:
        print(*edge)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
