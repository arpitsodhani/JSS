# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    MOD = 10 ** 9 + 7

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    tests = []
    mx = 0
    p = 1
    for _ in range(t):
        n, l, r = data[p], data[p + 1], data[p + 2]
        p += 3
        tests.append((n, l, r))
        if n > mx:
            mx = n

    fact = [1] * (mx + 1)
    for i in range(1, mx + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (mx + 1)
    invfact[mx] = pow(fact[mx], MOD - 2, MOD)
    for i in range(mx, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

    out = []
    for n, l, r in tests:
        half = n // 2
        st = min(1 - l, r - n)

        ans = st % MOD * comb(n, half) % MOD
        if n & 1:
            ans = (ans + st % MOD * comb(n, half + 1)) % MOD

        k = st + 1
        while True:
            lf = max(1, l + k)
            rg = min(n, r - k)
            cnt = rg + 1 - lf
            if cnt < 0:
                break

            forced = lf - 1
            ans = (ans + comb(cnt, half - forced)) % MOD
            if n & 1:
                ans = (ans + comb(cnt, half + 1 - forced)) % MOD
            k += 1

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
