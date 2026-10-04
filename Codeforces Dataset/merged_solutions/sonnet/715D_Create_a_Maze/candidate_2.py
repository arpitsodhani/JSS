# CLAUSE: setup_environment
import sys
from math import comb

# CLAUSE: solve_logic
def main():
    x = int(sys.stdin.readline())
    n = 32
    m = 32
    open_edges = set()

    def add_edge(a, b, c, d):
        open_edges.add((a, b, c, d))
        open_edges.add((c, d, a, b))

    for j in range(1, m):
        add_edge(1, j, 1, j + 1)

    for i in range(2, n + 1):
        for j in range(1, m):
            add_edge(i, j, i, j + 1)

    for i in range(1, n):
        for j in range(2, m):
            add_edge(i, j, i + 1, j)

    remaining = x
    taps = []
    for s in range(60, -1, -1):
        chosen = None
        for r in range(max(0, s - 30), min(30, s) + 1):
            value = comb(s, r)
            if value <= remaining and (chosen is None or value > chosen[0]):
                chosen = (value, r)
        if chosen is not None:
            value, r = chosen
            taps.append((r + 2, s - r + 2))
            remaining -= value
            if remaining == 0:
                break

    for i, j in taps:
        add_edge(i, j, i, j + 1)

    locks = []
    for i in range(1, n + 1):
        for j in range(1, m):
            edge = (i, j, i, j + 1)
            if edge not in open_edges:
                locks.append(edge)
    for i in range(1, n):
        for j in range(1, m + 1):
            edge = (i, j, i + 1, j)
            if edge not in open_edges:
                locks.append(edge)

    out = [str(n) + " " + str(m), str(len(locks))]
    out.extend(" ".join(map(str, edge)) for edge in locks)
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
