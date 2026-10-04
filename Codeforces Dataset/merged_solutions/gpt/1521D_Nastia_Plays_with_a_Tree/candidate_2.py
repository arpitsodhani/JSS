# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
sys.setrecursionlimit(300000)

def main():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        g = [[] for _ in range(n + 1)]
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
            edges.append((u, v))
        removed = []
        free = []

        def dfs(v, p):
            children = []
            for to in g[v]:
                if to != p:
                    end = dfs(to, v)
                    children.append((to, end))
            limit = 2 if p == 0 else 1
            while len(children) > limit:
                to, end = children.pop()
                removed.append((v, to))
                free.append(end)
            if not children:
                return v
            return children[0][1]
        root_end = dfs(1, 0)
        free.append(root_end)
        out.append(str(len(removed)))
        for i, (a, b) in enumerate(removed):
            out.append(f'{a} {b} {free[i]} {free[i + 1]}')
    print('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
