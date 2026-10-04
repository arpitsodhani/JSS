# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 1000000007

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    tests = []
    mx = 0
    p = 1

    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        k = data[p + 2] - 1
        p += 3
        tests.append((n, m, k))
        mx = max(mx, n + m)

    inv = [0] * (mx + 2)
    inv[1] = 1
    for i in range(2, mx + 2):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD

    out = []
    for n, m, k in tests:
        if n * m <= k:
            out.append("0")
            continue

        ans = 1

        for i in range(1, n):
            j = k // i
            if j < m:
                ans += inv[i + j]
                if ans >= MOD:
                    ans -= MOD

        for i in range(1, m):
            j = k // i
            if j < n:
                ans += inv[i + j]
                if ans >= MOD:
                    ans -= MOD

        out.append(str(ans % MOD))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
