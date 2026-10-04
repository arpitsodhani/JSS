# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import deque

    def main():
        input = sys.stdin.readline
        n, m = map(int, input().split())
        adj = [[] for _ in range(n)]
        edges = []

        for i in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * n
        color[0] = 0
        q = deque([0])

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return

        ans = []
        for u, v in edges:
            ans.append('1' if color[u] == 0 else '0')

        print("YES")
        print(''.join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
