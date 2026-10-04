# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    t = raw[2]
    graph = [[] for _ in range(n + 1)]
    i = 3
    for _ in range(m):
        graph[raw[i]].append((raw[i + 1], raw[i + 2]))
        i += 3

    inf = 10 ** 30
    distances = [inf] * (n + 1)
    distances[1] = 0
    parents = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
    longest = 1 if n == 1 else 0

    for used in range(1, n):
        nxt = [inf] * (n + 1)
        for u in range(1, n + 1):
            base = distances[u]
            if base == inf:
                continue
            for v, w in graph[u]:
                candidate = base + w
                if candidate < nxt[v]:
                    nxt[v] = candidate
                    parents[used + 1][v] = u
        if nxt[n] <= t:
            longest = used + 1
        distances = nxt

    ans = [0] * longest
    cur = n
    k = longest
    while k:
        ans[k - 1] = cur
        cur = parents[k][cur]
        k -= 1

    print(longest)
    print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
