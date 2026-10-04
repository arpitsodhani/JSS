# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n, m, total_time = values[:3]
    incoming = [[] for _ in range(n + 1)]
    p = 3
    for _ in range(m):
        u = values[p]
        v = values[p + 1]
        w = values[p + 2]
        incoming[v].append((u, w))
        p += 3
    return n, total_time, incoming

def main():
    n, total_time, incoming = read_input()
    inf = 10 ** 30
    old = [inf] * (n + 1)
    old[1] = 0
    parent = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
    answer = 1 if n == 1 else 0

    step = 2
    while step <= n:
        new = [inf] * (n + 1)
        for v in range(1, n + 1):
            best_cost = inf
            best_parent = 0
            for u, w in incoming[v]:
                value = old[u] + w
                if value < best_cost:
                    best_cost = value
                    best_parent = u
            new[v] = best_cost
            parent[step][v] = best_parent
        if new[n] <= total_time:
            answer = step
        old = new
        step += 1

    path = []
    vertex = n
    for step in range(answer, 0, -1):
        path.append(vertex)
        vertex = parent[step][vertex]
    path.reverse()

    sys.stdout.write("{}\n{}".format(answer, " ".join(map(str, path))))

# CLAUSE: finish_program
main()
