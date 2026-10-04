import sys

data = list(map(int, sys.stdin.buffer.read().split()))
q = data[0]
idx = 1
ans = []

INF = 10**9

for _ in range(q):
    n = data[idx]
    idx += 1
    t = data[idx:idx + n]
    idx += n
    t.sort()

    dp = [INF] * (n + 1)
    dp[0] = 0

    for minute in range(1, 2 * n + 1):
        ndp = dp[:]
        for used in range(1, n + 1):
            cost = dp[used - 1] + abs(t[used - 1] - minute)
            if cost < ndp[used]:
                ndp[used] = cost
        dp = ndp

    ans.append(str(dp[n]))

sys.stdout.write("\n".join(ans))
