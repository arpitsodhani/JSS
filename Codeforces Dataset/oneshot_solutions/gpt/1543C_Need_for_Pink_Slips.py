import sys

EPS = 1e-12

def expected(c, m, p, v):
    ans = 0.0

    def dfs(c, m, p, prob, depth):
        nonlocal ans
        ans += prob * p * depth

        if c > EPS:
            take = min(c, v)
            nc = c - take
            nm = m
            np = p
            if m > EPS:
                nm += take / 2.0
                np += take / 2.0
            else:
                np += take
            dfs(nc, nm, np, prob * c, depth + 1)

        if m > EPS:
            take = min(m, v)
            nc = c
            nm = m - take
            np = p
            if c > EPS:
                nc += take / 2.0
                np += take / 2.0
            else:
                np += take
            dfs(nc, nm, np, prob * m, depth + 1)

    dfs(c, m, p, 1.0, 1)
    return ans

data = sys.stdin.read().strip().split()
if data:
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        c, m, p, v = map(float, data[idx:idx + 4])
        idx += 4
        out.append(f"{expected(c, m, p, v):.12f}")
    print("\n".join(out))
