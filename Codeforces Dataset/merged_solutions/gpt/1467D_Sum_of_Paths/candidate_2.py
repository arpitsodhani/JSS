# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 10 ** 9 + 7

def main():
    input = sys.stdin.readline
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        weight = 1 if k == 0 else 0
        ans = a[0] * weight % MOD
        out = []
        for _ in range(q):
            idx, val = map(int, input().split())
            a[0] = val
            ans = val * weight % MOD
            out.append(str(ans))
        print('\n'.join(out))
        return
    dp = [[0] * n for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = 1
    for step in range(1, k + 1):
        prev = dp[step - 1]
        cur = dp[step]
        cur[0] = prev[1]
        cur[n - 1] = prev[n - 2]
        for i in range(1, n - 1):
            cur[i] = (prev[i - 1] + prev[i + 1]) % MOD
    weight = [0] * n
    for step in range(k + 1):
        left = dp[step]
        right = dp[k - step]
        for i in range(n):
            weight[i] = (weight[i] + left[i] * right[i]) % MOD
    ans = 0
    for i in range(n):
        ans = (ans + a[i] * weight[i]) % MOD
    out = []
    for _ in range(q):
        idx, val = map(int, input().split())
        idx -= 1
        ans = (ans + (val - a[idx]) * weight[idx]) % MOD
        a[idx] = val
        out.append(str(ans))
    print('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
