# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, m = data[0], data[1]
        adj = [[] for _ in range(n)]

        idx = 2
        for _ in range(m):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            adj[u].append(v)
            adj[v].append(u)

        root = max(range(n), key=lambda x: len(adj[x]))

        visited = [False] * n
        visited[root] = True
        ans = []
        q = deque()

        for v in adj[root]:
            if not visited[v]:
                visited[v] = True
                ans.append((root + 1, v + 1))
                q.append(v)

        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    ans.append((u + 1, v + 1))
                    q.append(v)

        sys.stdout.write("\n".join(f"{u} {v}" for u, v in ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
