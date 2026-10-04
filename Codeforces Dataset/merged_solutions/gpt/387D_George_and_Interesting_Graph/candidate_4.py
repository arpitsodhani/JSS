# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import deque

    def hopcroft_karp(adj, n, banned):
        pair_u = [0] * (n + 1)
        pair_v = [0] * (n + 1)
        dist = [0] * (n + 1)

        def bfs():
            q = deque()
            for u in range(1, n + 1):
                if u == banned:
                    continue
                if pair_u[u] == 0:
                    dist[u] = 0
                    q.append(u)
                else:
                    dist[u] = -1
            found = False
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v == banned:
                        continue
                    pu = pair_v[v]
                    if pu == 0:
                        found = True
                    elif dist[pu] == -1:
                        dist[pu] = dist[u] + 1
                        q.append(pu)
            return found

        def dfs(u):
            for v in adj[u]:
                if v == banned:
                    continue
                pu = pair_v[v]
                if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = -1
            return False

        matching = 0
        while bfs():
            for u in range(1, n + 1):
                if u != banned and pair_u[u] == 0 and dfs(u):
                    matching += 1
        return matching

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, m = data[0], data[1]
        edges = data[2:]

        has = [[False] * (n + 1) for _ in range(n + 1)]
        adj = [[] for _ in range(n + 1)]

        for i in range(0, 2 * m, 2):
            a, b = edges[i], edges[i + 1]
            has[a][b] = True
            adj[a].append(b)

        ans = 10 ** 18
        final_edges = 3 * n - 2

        for center in range(1, n + 1):
            keep_star = 1 if has[center][center] else 0
            for u in range(1, n + 1):
                if u != center:
                    if has[u][center]:
                        keep_star += 1
                    if has[center][u]:
                        keep_star += 1

            keep_matching = hopcroft_karp(adj, n, center)
            kept = keep_star + keep_matching
            ans = min(ans, m + final_edges - 2 * kept)

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
