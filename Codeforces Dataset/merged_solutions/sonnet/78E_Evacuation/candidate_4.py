# CLAUSE: setup_environment
import sys
from collections import deque

INF = 1000000000

def add_edge(g, v, u, c):
    g[v].append([u, c, len(g[u])])
    g[u].append([v, 0, len(g[v]) - 1])

def dinic(g, s, t):
    total = 0
    n = len(g)
    sys.setrecursionlimit(1000000)
    def dfs(v, f):
        if v == t:
            return f
        while ptr[v] < len(g[v]):
            e = g[v][ptr[v]]
            if e[1] > 0 and level[e[0]] == level[v] + 1:
                got = dfs(e[0], min(f, e[1]))
                if got:
                    e[1] -= got
                    g[e[0]][e[2]][1] += got
                    return got
            ptr[v] += 1
        return 0
    while True:
        level = [-1] * n
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to, cap, rev in g[v]:
                if cap > 0 and level[to] == -1:
                    level[to] = level[v] + 1
                    q.append(to)
        if level[t] == -1:
            return total
        ptr = [0] * n
        while True:
            cur = dfs(s, INF)
            if cur == 0:
                break
            total += cur

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.read().split()
    if not raw:
        return
    n = int(raw[0])
    t = int(raw[1])
    caps = raw[2:2 + n]
    scis = raw[2 + n:2 + 2 * n]
    cells = n * n
    open_cell = [True] * cells
    poison = [INF] * cells
    source_reactors = []
    scientists = []
    capsules = []
    for i in range(n):
        for j in range(n):
            k = i * n + j
            c = caps[i][j]
            if c in "YZ":
                open_cell[k] = False
                if c == "Z":
                    poison[k] = 0
                    source_reactors.append(k)
            else:
                v = int(c)
                if v:
                    capsules.append((k, v))
            s = scis[i][j]
            if s not in "YZ":
                v = int(s)
                if v:
                    scientists.append((k, v))
    q = deque(source_reactors)
    while q:
        k = q.popleft()
        x, y = divmod(k, n)
        nd = poison[k] + 1
        for nk in (k - n, k + n, k - 1, k + 1):
            if nk < 0 or nk >= cells:
                continue
            nx, ny = divmod(nk, n)
            if abs(nx - x) + abs(ny - y) == 1 and open_cell[nk] and poison[nk] == INF:
                poison[nk] = nd
                q.append(nk)
    a = len(scientists)
    b = len(capsules)
    src = a + b
    sink = src + 1
    graph = [[] for _ in range(sink + 1)]
    for i, (cell, count) in enumerate(scientists):
        add_edge(graph, src, i, count)
    for j, (cell, count) in enumerate(capsules):
        add_edge(graph, a + j, sink, count)
    cap_index = {cell: [] for cell, count in capsules}
    for j, (cell, count) in enumerate(capsules):
        cap_index[cell].append(j)
    for i, (start, count) in enumerate(scientists):
        dist = [-1] * cells
        q = deque()
        if poison[start] > 0:
            dist[start] = 0
            q.append(start)
        seen_caps = set()
        while q:
            k = q.popleft()
            if k in cap_index:
                for j in cap_index[k]:
                    if j not in seen_caps:
                        seen_caps.add(j)
                        add_edge(graph, i, a + j, INF)
            x, y = divmod(k, n)
            nd = dist[k] + 1
            if nd > t:
                continue
            for nk in (k - n, k + n, k - 1, k + 1):
                if nk < 0 or nk >= cells:
                    continue
                nx, ny = divmod(nk, n)
                if abs(nx - x) + abs(ny - y) == 1 and open_cell[nk] and dist[nk] == -1 and nd < poison[nk]:
                    dist[nk] = nd
                    q.append(nk)
    print(dinic(graph, src, sink))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
