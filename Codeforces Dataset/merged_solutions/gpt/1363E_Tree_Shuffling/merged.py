# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    input = sys.stdin.readline
    n = int(input())
    a = [0] * n
    b = [0] * n
    c = [0] * n

    sb = sc = 0
    for i in range(n):
        a[i], b[i], c[i] = map(int, input().split())
        sb += b[i]
        sc += c[i]

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    if sb != sc:
        print(-1)
        return

    parent = [-1] * n
    mn = [0] * n
    order = [0]
    parent[0] = -2
    mn[0] = a[0]

    for u in order:
        for v in g[u]:
            if parent[v] == -1:
                parent[v] = u
                mn[v] = min(mn[u], a[v])
                order.append(v)

    need01 = [0] * n
    need10 = [0] * n
    ans = 0

    for u in reversed(order):
        x = 1 if b[u] == 0 and c[u] == 1 else 0
        y = 1 if b[u] == 1 and c[u] == 0 else 0

        for v in g[u]:
            if parent[v] == u:
                x += need01[v]
                y += need10[v]

        t = min(x, y)
        ans += 2 * t * mn[u]
        need01[u] = x - t
        need10[u] = y - t

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
