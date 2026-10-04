# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    x = next(it)
    color = [next(it) for _ in range(n)]
    black = sum(color)

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        g[u].append((v, w))
        g[v].append((u, w))

    if black == 0:
        print(-1)
        return
    if black == n:
        print(0)
        return

    parent = [-1] * n
    order = [0]
    for v in order:
        for to, _ in g[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)

    inf = x + 1

    def prune(mp):
        by_count = {}
        for (cnt, d, r), val in mp.items():
            by_count.setdefault(cnt, []).append((d, r, val))

        res = {}
        for cnt, states in by_count.items():
            best = {}
            for d, r, val in states:
                key = (d, r)
                if val > best.get(key, -1):
                    best[key] = val

            items = [(d, r, val) for (d, r), val in best.items()]
            m = len(items)
            for i in range(m):
                d, r, val = items[i]
                ok = True
                for j in range(m):
                    if i == j:
                        continue
                    d2, r2, val2 = items[j]
                    if d2 <= d and r2 <= r and val2 >= val and (d2 < d or r2 < r or val2 > val):
                        ok = False
                        break
                if ok:
                    res[(cnt, d, r)] = val
        return res

    dp = [None] * n

    for v in reversed(order):
        cur = {
            (0, inf, 0): 0,
            (1, 0, -1): color[v],
        }

        for to, w in g[v]:
            if parent[to] != v:
                continue

            nxt = {}
            for (c1, d1, r1), val1 in cur.items():
                for (c2, d2, r2), val2 in dp[to].items():
                    cnt = c1 + c2
                    if cnt > black:
                        continue

                    if d2 == inf or d2 + w > x:
                        sd2 = inf
                    else:
                        sd2 = d2 + w

                    if r2 == -1:
                        sr2 = -1
                    else:
                        sr2 = r2 + w
                        if sr2 > x:
                            continue

                    nr1 = r1
                    if nr1 != -1 and sd2 != inf and sd2 + nr1 <= x:
                        nr1 = -1

                    nr2 = sr2
                    if nr2 != -1 and d1 != inf and d1 + nr2 <= x:
                        nr2 = -1

                    key = (cnt, min(d1, sd2), max(nr1, nr2))
                    val = val1 + val2
                    if val > nxt.get(key, -1):
                        nxt[key] = val

            cur = prune(nxt)

        dp[v] = cur

    best = -1
    for (cnt, _, r), val in dp[0].items():
        if cnt == black and r == -1 and val > best:
            best = val

    print(-1 if best < 0 else black - best)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
