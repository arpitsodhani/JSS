# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from collections import deque

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            it = iter(data)
            t = next(it)
            out = []

            for _ in range(t):
                n = next(it)
                q = next(it)

                g = [[] for _ in range(n)]
                for _ in range(n - 1):
                    u = next(it) - 1
                    v = next(it) - 1
                    g[u].append(v)
                    g[v].append(u)

                parent = [-1] * n
                depth = [0] * n
                order = [0]
                parent[0] = 0

                for v in order:
                    for to in g[v]:
                        if parent[to] == -1:
                            parent[to] = v
                            depth[to] = depth[v] + 1
                            order.append(to)

                seen = [0] * (n + 1)
                stamp = 0

                for _ in range(q):
                    a = [next(it) for _ in range(n)]
                    u = next(it) - 1
                    v = next(it) - 1

                    stamp += 1
                    x, y = u, v

                    while depth[x] > depth[y]:
                        seen[a[x]] = stamp
                        x = parent[x]
                    while depth[y] > depth[x]:
                        seen[a[y]] = stamp
                        y = parent[y]
                    while x != y:
                        seen[a[x]] = stamp
                        seen[a[y]] = stamp
                        x = parent[x]
                        y = parent[y]

                    seen[a[x]] = stamp

                    mex = 0
                    while seen[mex] == stamp:
                        mex += 1

                    out.append(str(mex))

            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
