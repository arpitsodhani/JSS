import sys

def solve():
    data = sys.stdin.read().split()
    t = int(data[0])
    p = 1
    ans = []
    neg = -10**9

    for _ in range(t):
        n = int(data[p])
        x = int(data[p + 1])
        s = int(data[p + 2])
        u = data[p + 3]
        p += 4

        dp = [neg] * (x + 1)
        dp[0] = 0
        lim = 0

        for ch in u:
            ndp = dp[:]
            if ch == 'I':
                for k in range(lim + 1):
                    c = dp[k]
                    if c >= 0 and k < x and c + 1 > ndp[k + 1]:
                        ndp[k + 1] = c + 1
                if lim < x:
                    lim += 1
            elif ch == 'E':
                for k in range(lim + 1):
                    c = dp[k]
                    if c >= 0 and c < k * s and c + 1 > ndp[k]:
                        ndp[k] = c + 1
            else:
                old_lim = lim
                for k in range(old_lim + 1):
                    c = dp[k]
                    if c < 0:
                        continue
                    if c < k * s and c + 1 > ndp[k]:
                        ndp[k] = c + 1
                    if k < x and c + 1 > ndp[k + 1]:
                        ndp[k + 1] = c + 1
                if lim < x:
                    lim += 1
            dp = ndp

        ans.append(str(max(dp)))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
