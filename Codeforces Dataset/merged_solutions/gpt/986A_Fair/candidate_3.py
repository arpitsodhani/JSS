# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        it = iter(data)
        n = next(it)
        m = next(it)
        k = next(it)
        s = next(it)

        types = [next(it) - 1 for _ in range(n)]
        by_type = [[] for _ in range(k)]
        for i, t in enumerate(types):
            by_type[t].append(i)

        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = next(it) - 1
            v = next(it) - 1
            adj[u].append(v)
            adj[v].append(u)

        vals = [[] for _ in range(n)]
        dist = [-1] * n

        for goods in range(k):
            q = deque()
            touched = []

            for v in by_type[goods]:
                dist[v] = 0
                q.append(v)
                touched.append(v)

            while q:
                v = q.popleft()
                nd = dist[v] + 1
                for to in adj[v]:
                    if dist[to] == -1:
                        dist[to] = nd
                        q.append(to)
                        touched.append(to)

            for v in touched:
                vals[v].append(dist[v])
                dist[v] = -1

        ans = []
        for arr in vals:
            arr.sort()
            ans.append(str(sum(arr[:s])))

        sys.stdout.write(" ".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
