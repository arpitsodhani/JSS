# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n, m, max_time = nums[0], nums[1], nums[2]
    edges = [None] * m
    at = 3
    for j in range(m):
        edges[j] = (nums[at], nums[at + 1], nums[at + 2])
        at += 3

    inf = 10 ** 30
    current = [inf] * (n + 1)
    current[1] = 0
    trace = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
    best_len = int(n == 1)

    for size in range(2, n + 1):
        next_cost = [inf] * (n + 1)
        next_parent = trace[size]
        for edge in edges:
            u, v, w = edge
            value = current[u] + w
            if value < next_cost[v]:
                next_cost[v] = value
                next_parent[v] = u
        if next_cost[n] <= max_time:
            best_len = size
        current = next_cost

    result = array("H", [0]) * best_len
    vertex = n
    for size in range(best_len, 0, -1):
        result[size - 1] = vertex
        vertex = trace[size][vertex]

    out = [str(best_len), " ".join(str(x) for x in result)]
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
