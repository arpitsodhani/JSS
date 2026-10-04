# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    costs = [[int(raw[1 + color * n + i]) for i in range(n)] for color in range(3)]
    edge_start = 1 + 3 * n

    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        u = int(raw[edge_start + 2 * i]) - 1
        v = int(raw[edge_start + 2 * i + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)

    if n == 1:
        color = sorted(range(3), key=lambda x: costs[x][0])[0]
        print(costs[color][0])
        print(color + 1)
        return

    if n == 2:
        first = sorted(range(3), key=lambda x: costs[x][0])[0]
        second = sorted(range(3), key=lambda x: costs[x][1])[0]
        print(costs[first][0] + costs[second][1])
        print(first + 1, second + 1)
        return

    ends = []
    for i in range(n):
        if len(adj[i]) > 2:
            print(-1)
            return
        if len(adj[i]) == 1:
            ends.append(i)

    order = []
    seen = [False] * n
    q = deque([(ends[0], -1)])
    while q:
        node, parent = q.popleft()
        order.append(node)
        seen[node] = True
        for nxt in adj[node]:
            if nxt != parent:
                q.append((nxt, node))
                break

    patterns = [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ]

    best_total = 10 ** 30
    best_colors = []
    for pattern in patterns:
        total = 0
        assigned = [0] * n
        for pos in range(n):
            vertex = order[pos]
            color = pattern[pos % 3]
            assigned[vertex] = color + 1
            total += costs[color][vertex]
        if total < best_total:
            best_total = total
            best_colors = assigned

    output = [str(best_total), " ".join(str(x) for x in best_colors)]
    sys.stdout.write("\n".join(output) + "\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
