# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    input = sys.stdin.readline
    n, a = map(int, input().split())
    d = [0] * n
    b = [0] * n
    for i in range(n):
        di, ci = map(int, input().split())
        d[i] = di
        b[i] = a - ci

    parent = list(range(n))
    size = [1] * n
    total = b[:]
    pref = b[:]
    suff = b[:]
    best = b[:]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def unite(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return rx

        if x > y:
            rx, ry = ry, rx

        parent[ry] = rx
        size[rx] += size[ry]

        total_rx = total[rx]
        total_ry = total[ry]

        pref[rx] = max(pref[rx], total_rx + pref[ry])
        suff[rx] = max(suff[ry], total_ry + suff[rx])
        best[rx] = max(best[rx], best[ry], suff[rx] + pref[ry] - total_ry)
        total[rx] = total_rx + total_ry

        return rx

    ans = max(0, max(b))

    edges = []
    for i in range(n - 1):
        gap = d[i + 1] - d[i]
        edges.append((gap * gap, i))
    edges.sort()

    i = 0
    while i < len(edges):
        w = edges[i][0]
        changed = []
        while i < len(edges) and edges[i][0] == w:
            root = unite(edges[i][1], edges[i][1] + 1)
            changed.append(root)
            i += 1
        for root in changed:
            root = find(root)
            val = best[root] - w
            if val > ans:
                ans = val

    print(ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
