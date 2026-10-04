# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    qs = []
    mx = 0
    p = 1
    for _ in range(t):
        n, m, k = data[p], data[p + 1], data[p + 2]
        p += 3
        qs.append((n, m, k))
        if k > mx:
            mx = k

    st = [[0] * (mx + 1) for _ in range(mx + 1)]
    st[0][0] = 1
    for i in range(1, mx + 1):
        row = st[i]
        prev = st[i - 1]
        for j in range(1, i + 1):
            row[j] = (prev[j - 1] + j * prev[j]) % MOD

    out = []
    for n, m, k in qs:
        odd = (m + 1) // 2 % MOD
        mm = m % MOD
        lim = min(k, n)

        ans = 0
        fall = 1
        odd_pow = 1
        m_pow = pow(mm, n, MOD)
        inv_m = pow(mm, MOD - 2, MOD)

        for j in range(lim + 1):
            ans = (ans + st[k][j] * fall % MOD * odd_pow % MOD * m_pow) % MOD
            if j != lim:
                fall = fall * ((n - j) % MOD) % MOD
                odd_pow = odd_pow * odd % MOD
                m_pow = m_pow * inv_m % MOD

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
