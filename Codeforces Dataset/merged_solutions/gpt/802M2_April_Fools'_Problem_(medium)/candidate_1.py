# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]
    a = data[2:2 + n]
    b = data[2 + n:2 + 2 * n]

    s = 0
    t = n + 1
    g = [[] for _ in range(n + 2)]

    def add(u, v, cap, cost):
        g[u].append([v, cap, cost, len(g[v])])
        g[v].append([u, 0, -cost, len(g[u]) - 1])

    inf = 10 ** 9

    for i in range(n):
        day = i + 1
        add(s, day, 1, a[i])
        add(day, t, 1, b[i])
        if day < n:
            add(day, day + 1, inf, 0)

    pot = [0] * (n + 2)
    ans = 0
    flow = 0

    while flow < k:
        dist = [10 ** 30] * (n + 2)
        pv = [-1] * (n + 2)
        pe = [-1] * (n + 2)
        dist[s] = 0
        heap = [(0, s)]

        while heap:
            d, v = heapq.heappop(heap)
            if d != dist[v]:
                continue
            for idx, e in enumerate(g[v]):
                if e[1] <= 0:
                    continue
                to, cap, cost, rev = e
                nd = d + cost + pot[v] - pot[to]
                if nd < dist[to]:
                    dist[to] = nd
                    pv[to] = v
                    pe[to] = idx
                    heapq.heappush(heap, (nd, to))

        for i in range(n + 2):
            if dist[i] < 10 ** 30:
                pot[i] += dist[i]

        addflow = k - flow
        v = t
        while v != s:
            e = g[pv[v]][pe[v]]
            if e[1] < addflow:
                addflow = e[1]
            v = pv[v]

        v = t
        while v != s:
            e = g[pv[v]][pe[v]]
            e[1] -= addflow
            g[v][e[3]][1] += addflow
            ans += addflow * e[2]
            v = pv[v]

        flow += addflow

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
