# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, limit = data[0], data[1], data[2]
    pos = 3
    edges = []
    for _ in range(m):
        edges.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3

    inf = 10 ** 30
    prev = [inf] * (n + 1)
    prev[1] = 0
    parent = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
    best = 1 if n == 1 else 0

    for length in range(2, n + 1):
        cur = [inf] * (n + 1)
        for u, v, w in edges:
            cost = prev[u] + w
            if cost < cur[v]:
                cur[v] = cost
                parent[length][v] = u
        if cur[n] <= limit:
            best = length
        prev = cur

    route = [0] * best
    node = n
    for length in range(best, 0, -1):
        route[length - 1] = node
        node = parent[length][node]

    sys.stdout.write(str(best) + "\n" + " ".join(map(str, route)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
