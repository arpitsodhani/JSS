# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import heapq

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            it = iter(data)
            n = next(it)
            m = next(it)
            x = next(it) - 1
            y = next(it) - 1

            g = [[] for _ in range(n)]
            for _ in range(m):
                a = next(it) - 1
                b = next(it) - 1
                w = next(it)
                g[a].append((b, w))
                g[b].append((a, w))

            t = [0] * n
            c = [0] * n
            for i in range(n):
                t[i] = next(it)
                c[i] = next(it)

            inf = 10 ** 30
            ans = [inf] * n
            ans[x] = 0
            pq = [(0, x)]
            used = [False] * n

            while pq:
                cur, v = heapq.heappop(pq)
                if cur != ans[v] or used[v]:
                    continue
                if v == y:
                    print(cur)
                    return

                used[v] = True

                lim = t[v]
                d = [inf] * n
                d[v] = 0
                q = [(0, v)]

                while q:
                    dist, u = heapq.heappop(q)
                    if dist != d[u]:
                        continue
                    if dist > lim:
                        continue
                    if cur + c[v] < ans[u]:
                        ans[u] = cur + c[v]
                        heapq.heappush(pq, (ans[u], u))
                    for to, w in g[u]:
                        nd = dist + w
                        if nd <= lim and nd < d[to]:
                            d[to] = nd
                            heapq.heappush(q, (nd, to))

            print(-1)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
