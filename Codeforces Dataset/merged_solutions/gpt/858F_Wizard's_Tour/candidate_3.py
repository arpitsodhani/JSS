# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    sys.setrecursionlimit(1000000)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n, m = data[0], data[1]
        adj = [[] for _ in range(n)]
        p = 2
        for i in range(m):
            a = data[p] - 1
            b = data[p + 1] - 1
            p += 2
            adj[a].append((b, i))
            adj[b].append((a, i))

        used = [False] * m
        seen = [False] * n
        ans = []

        def dfs(u):
            seen[u] = True
            pending = []

            for v, eid in adj[u]:
                if used[eid]:
                    continue
                used[eid] = True
                if not seen[v]:
                    child = dfs(v)
                    if child != -1:
                        pending.append(child)
                    else:
                        pending.append(v)
                else:
                    pending.append(v)

            while len(pending) >= 2:
                a = pending.pop()
                b = pending.pop()
                ans.append((a + 1, u + 1, b + 1))

            if pending:
                return pending[0]
            return -1

        for i in range(n):
            if not seen[i]:
                dfs(i)

        out = [str(len(ans))]
        out.extend(f"{a} {b} {c}" for a, b, c in ans)
        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
