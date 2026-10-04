import sys

INF = 10 ** 9

def solve_case(p):
    n = len(p)
    vals = [0] + p + [n + 1]
    m = n + 2

    dp = [INF] * m
    dp[0] = 0
    for j in range(1, m):
        if vals[j - 1] < vals[j]:
            dp[j] = dp[j - 1]

    exact = [dp[-1]]
    size = n + 3

    for _ in range(1, n + 1):
        prev = dp
        cur = [INF] * m
        bit = [INF] * (size + 1)

        def update(i, x):
            while i <= size:
                if x < bit[i]:
                    bit[i] = x
                i += i & -i

        def query(i):
            res = INF
            while i > 0:
                if bit[i] < res:
                    res = bit[i]
                i -= i & -i
            return res

        for j in range(1, m):
            i = j - 2
            if i >= 0 and prev[i] < INF:
                update(vals[i] + 1, prev[i] - i)

            best = query(vals[j])
            if best < INF:
                cur[j] = best + j - 1

            if vals[j - 1] < vals[j] and cur[j - 1] < cur[j]:
                cur[j] = cur[j - 1]

        dp = cur
        exact.append(dp[-1])

    ans = []
    best = INF
    for k in range(1, n + 1):
        if exact[k - 1] < best:
            best = exact[k - 1]
        if exact[k] < best:
            best = exact[k]
        ans.append(str(best))

    return " ".join(ans)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx:idx + n]
        idx += n
        out.append(solve_case(p))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
