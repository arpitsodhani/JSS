# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import deque
        import heapq

        def dinic(n, cap):
            g = [[] for _ in range(n)]

            def add(u, v, c):
                g[u].append([v, c, len(g[v])])
                g[v].append([u, 0, len(g[u]) - 1])

            for i in range(n):
                for j in range(n):
                    if cap[i][j]:
                        add(i, j, cap[i][j])

            flow = 0
            s, t = 0, n - 1

            while True:
                level = [-1] * n
                level[s] = 0
                q = deque([s])
                while q:
                    v = q.popleft()
                    for to, c, _ in g[v]:
                        if c > 0 and level[to] < 0:
                            level[to] = level[v] + 1
                            q.append(to)
                if level[t] < 0:
                    break

                it = [0] * n

                def dfs(v, f):
                    if v == t:
                        return f
                    while it[v] < len(g[v]):
                        e = g[v][it[v]]
                        if e[1] > 0 and level[v] + 1 == level[e[0]]:
                            ret = dfs(e[0], min(f, e[1]))
                            if ret:
                                e[1] -= ret
                                g[e[0]][e[2]][1] += ret
                                return ret
                        it[v] += 1
                    return 0

                while True:
                    pushed = dfs(s, 10 ** 30)
                    if not pushed:
                        break
                    flow += pushed

            return flow

        def can(n, cap, need, k):
            g = [[] for _ in range(n)]
            inf = 10 ** 18

            def add(u, v, c, w):
                g[u].append([v, len(g[v]), c, w])
                g[v].append([u, len(g[u]) - 1, 0, -w])

            for i in range(n):
                for j in range(n):
                    if cap[i][j]:
                        add(i, j, cap[i][j], 0)
                        add(i, j, inf, 1)

            s, t = 0, n - 1
            pot = [0] * n
            flow = 0
            cost = 0

            while flow < need:
                dist = [inf] * n
                pv = [-1] * n
                pe = [-1] * n
                dist[s] = 0
                pq = [(0, s)]

                while pq:
                    d, v = heapq.heappop(pq)
                    if d != dist[v]:
                        continue
                    for i, e in enumerate(g[v]):
                        if e[2] <= 0:
                            continue
                        nd = d + e[3] + pot[v] - pot[e[0]]
                        if nd < dist[e[0]]:
                            dist[e[0]] = nd
                            pv[e[0]] = v
                            pe[e[0]] = i
                            heapq.heappush(pq, (nd, e[0]))

                if dist[t] == inf:
                    return False

                for i in range(n):
                    if dist[i] < inf:
                        pot[i] += dist[i]

                addf = need - flow
                v = t
                while v != s:
                    e = g[pv[v]][pe[v]]
                    addf = min(addf, e[2])
                    v = pv[v]

                if pot[t] > 0:
                    addf = min(addf, (k - cost) // pot[t] + 1)

                v = t
                while v != s:
                    e = g[pv[v]][pe[v]]
                    e[2] -= addf
                    g[v][e[1]][2] += addf
                    v = pv[v]

                flow += addf
                cost += addf * pot[t]

                if cost > k:
                    return False

            return True

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n, k = data[0], data[1]
            a = data[2:]
            cap = [a[i * n:(i + 1) * n] for i in range(n)]

            base = dinic(n, cap)
            lo, hi = 0, k

            while lo < hi:
                mid = (lo + hi + 1) // 2
                if can(n, cap, base + mid, k):
                    lo = mid
                else:
                    hi = mid - 1

            print(base + lo)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
