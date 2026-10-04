import sys

def main():
    input = sys.stdin.readline
    q = int(input())
    INF = 10**30
    ans = []

    for _ in range(q):
        n = int(input())
        a = []
        b = []
        for _ in range(n):
            x, y = map(int, input().split())
            a.append(x)
            b.append(y)

        dp = [0, b[0], 2 * b[0]]

        for i in range(1, n):
            ndp = [INF, INF, INF]
            for cur in range(3):
                for prev in range(3):
                    if a[i] + cur != a[i - 1] + prev:
                        cost = dp[prev] + cur * b[i]
                        if cost < ndp[cur]:
                            ndp[cur] = cost
            dp = ndp

        ans.append(str(min(dp)))

    print("\n".join(ans))

if __name__ == "__main__":
    main()
