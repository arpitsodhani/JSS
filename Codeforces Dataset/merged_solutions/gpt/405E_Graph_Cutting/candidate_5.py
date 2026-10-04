# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n, m = data[0], data[1]
            if m % 2:
                print("No solution")
                return

            adj = [[] for _ in range(n)]
            pos = 2
            for i in range(m):
                u = data[pos] - 1
                v = data[pos + 1] - 1
                pos += 2
                adj[u].append((v, i))
                adj[v].append((u, i))

            sys.setrecursionlimit(300000)
            used = [False] * m
            seen = [False] * n
            parent = [-1] * n
            ans = []
            bad = False

            def dfs(v, pe):
                nonlocal bad
                seen[v] = True
                rem = []

                for to, eid in adj[v]:
                    if eid == pe or used[eid]:
                        continue
                    used[eid] = True
                    if not seen[to]:
                        parent[to] = v
                        if dfs(to, eid):
                            rem.append(to)
                    else:
                        rem.append(to)

                while len(rem) >= 2:
                    a = rem.pop()
                    b = rem.pop()
                    ans.append((a + 1, v + 1, b + 1))

                if rem:
                    if pe == -1:
                        bad = True
                        return False
                    ans.append((rem[0] + 1, v + 1, parent[v] + 1))
                    return False

                return pe != -1

            dfs(0, -1)

            if bad or len(ans) * 2 != m:
                print("No solution")
            else:
                print("\n".join(f"{a} {b} {c}" for a, b, c in ans))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
