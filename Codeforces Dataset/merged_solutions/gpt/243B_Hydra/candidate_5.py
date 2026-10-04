# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        n, m, h, t = data[:4]
        adj = [set() for _ in range(n + 1)]
        edges = []
        p = 4

        for _ in range(m):
            u = data[p]
            v = data[p + 1]
            p += 2
            adj[u].add(v)
            adj[v].add(u)
            edges.append((u, v))

        def attempt(u, v):
            if len(adj[u]) - 1 < h or len(adj[v]) - 1 < t:
                return None

            common = []
            only_u = []
            only_v = []

            for x in adj[u]:
                if x == v:
                    continue
                if x in adj[v]:
                    common.append(x)
                else:
                    only_u.append(x)

            for x in adj[v]:
                if x == u:
                    continue
                if x not in adj[u]:
                    only_v.append(x)

            if len(only_u) + len(only_v) + len(common) < h + t:
                return None

            heads = []
            tails = []

            while only_u and len(heads) < h:
                heads.append(only_u.pop())

            while only_v and len(tails) < t:
                tails.append(only_v.pop())

            for x in common:
                if len(heads) < h:
                    heads.append(x)
                elif len(tails) < t:
                    tails.append(x)

            if len(heads) == h and len(tails) == t:
                return heads, tails
            return None

        for u, v in edges:
            res = attempt(u, v)
            if res is not None:
                heads, tails = res
                print("YES")
                print(u, v)
                print(*heads)
                print(*tails)
                sys.exit()

            res = attempt(v, u)
            if res is not None:
                heads, tails = res
                print("YES")
                print(v, u)
                print(*heads)
                print(*tails)
                sys.exit()

        print("NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
