# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 998244353

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    ans = []

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n
        b = data[p:p + n]
        p += n

        dp0 = 1
        dp1 = 1

        for i in range(1, n):
            ndp0 = 0
            ndp1 = 0

            if a[i - 1] <= a[i] and b[i - 1] <= b[i]:
                ndp0 = (ndp0 + dp0) % MOD
            if b[i - 1] <= a[i] and a[i - 1] <= b[i]:
                ndp0 = (ndp0 + dp1) % MOD
            if a[i - 1] <= b[i] and b[i - 1] <= a[i]:
                ndp1 = (ndp1 + dp0) % MOD
            if b[i - 1] <= b[i] and a[i - 1] <= a[i]:
                ndp1 = (ndp1 + dp1) % MOD

            dp0, dp1 = ndp0, ndp1

        ans.append(str((dp0 + dp1) % MOD))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
