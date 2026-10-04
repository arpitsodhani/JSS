import sys

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]

    cap = k
    dp = [0] * (n + 1)
    dp[0] = 1
    last = [[0] * (n + 1) for _ in range(26)]

    for i, ch in enumerate(s, 1):
        c = ord(ch) - 97
        for length in range(i, 0, -1):
            add = dp[length - 1]
            dp[length] += add - last[c][length]
            if dp[length] > cap:
                dp[length] = cap
            last[c][length] = add

    ans = 0
    need = k
    for length in range(n, -1, -1):
        take = min(need, dp[length])
        ans += take * (n - length)
        need -= take
        if need == 0:
            print(ans)
            return

    print(-1)

if __name__ == "__main__":
    main()
