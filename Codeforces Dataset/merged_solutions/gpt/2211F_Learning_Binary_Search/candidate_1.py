# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
MOD = 676767677

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    tests = [(data[i], data[i + 1]) for i in range(1, 2 * t, 2)]

    lim = 0
    for n, m in tests:
        v = 2 * n + m
        if v > lim:
            lim = v

    fact = array('I', [1]) * (lim + 1)
    for i in range(1, lim + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = array('I', [1]) * (lim + 1)
    invfact[lim] = pow(fact[lim], MOD - 2, MOD)
    for i in range(lim, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD

    out = []

    for n, m in tests:
        maxs = 2 * n - 2
        pb = array('I', [0]) * (maxs + 1)
        ps = array('I', [0]) * (maxs + 1)

        km3 = m - 3
        acc_b = 0
        acc_s = 0
        for s in range(1, maxs + 1):
            if s >= 2:
                b = comb(s + m - 2, km3)
                acc_b = (acc_b + b) % MOD
                acc_s = (acc_s + s * b) % MOD
            pb[s] = acc_b
            ps[s] = acc_s

        pref = array('I', [0]) * n
        km2 = m - 2
        acc = 0
        for i in range(1, n):
            acc = (acc + comb(i + m - 1, km2)) % MOD
            pref[i] = acc

        def sum_arr(arr, l, r):
            if r < l:
                return 0
            if l < 0:
                l = 0
            if r >= len(arr):
                r = len(arr) - 1
            if r < l:
                return 0
            res = arr[r]
            if l:
                res -= arr[l - 1]
            return res % MOD

        def h(u, v):
            if u <= 0 or v <= 0:
                return 0
            a = u if u < v else v
            b = v if u < v else u
            total = u + v
            res = (sum_arr(ps, 2, a + 1) - sum_arr(pb, 2, a + 1)) % MOD
            res = (res + a * sum_arr(pb, a + 2, b + 1)) % MOD
            res = (res + (total + 1) * sum_arr(pb, b + 2, total) - sum_arr(ps, b + 2, total)) % MOD
            return res

        def rect(a1, a2, d1, d2):
            if a1 > a2 or d1 > d2:
                return 0
            res = 0
            if a1 <= 0 <= a2 and d1 <= 0 <= d2:
                res += m
            if d1 <= 0 <= d2:
                lo = a1 if a1 > 1 else 1
                hi = a2
                if lo <= hi:
                    res += pref[hi] - pref[lo - 1]
            if a1 <= 0 <= a2:
                lo = d1 if d1 > 1 else 1
                hi = d2
                if lo <= hi:
                    res += pref[hi] - pref[lo - 1]
            ia1 = a1 if a1 > 1 else 1
            id1 = d1 if d1 > 1 else 1
            if ia1 <= a2 and id1 <= d2:
                res += h(a2, d2) - h(ia1 - 1, d2) - h(a2, id1 - 1) + h(ia1 - 1, id1 - 1)
            return res % MOD

        ans = 0
        stack = [(1, n, 0)]
        while stack:
            l, r, dep = stack.pop()
            p = (l + r) // 2
            ans = (ans + (dep + 1) * rect(l - 1, p - 1, n - r, n - p)) % MOD
            if l <= p - 1:
                stack.append((l, p - 1, dep + 1))
            if p + 1 <= r:
                stack.append((p + 1, r, dep + 1))

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
