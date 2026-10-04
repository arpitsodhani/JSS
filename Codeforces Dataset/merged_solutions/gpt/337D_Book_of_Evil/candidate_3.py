# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    def distances(start, graph):
        n = len(graph) - 1
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for to in graph[v]:
                if dist[to] == -1:
                    dist[to] = dist[v] + 1
                    q.append(to)
        return dist

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, d = data[0], data[1], data[2]
    special = data[3:3 + m]

    graph = [[] for _ in range(n + 1)]
    idx = 3 + m
    for _ in range(n - 1):
        a, b = data[idx], data[idx + 1]
        idx += 2
        graph[a].append(b)
        graph[b].append(a)

    dist0 = distances(special[0], graph)
    a = max(special, key=lambda x: dist0[x])

    dist_a = distances(a, graph)
    b = max(special, key=lambda x: dist_a[x])

    dist_b = distances(b, graph)

    ans = 0
    for i in range(1, n + 1):
        if max(dist_a[i], dist_b[i]) <= d:
            ans += 1

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
