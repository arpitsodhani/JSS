# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from array import array

    MOD = 998244353

    data = sys.stdin.buffer.read()
    idx = 0
    ln_data = len(data)

    def next_int():
        global idx
        while idx < ln_data and data[idx] <= 32:
            idx += 1
        sign = 1
        if data[idx] == 45:
            sign = -1
            idx += 1
        x = 0
        while idx < ln_data and data[idx] > 32:
            x = x * 10 + data[idx] - 48
            idx += 1
        return x * sign

    t = next_int()
    out = []

    for _ in range(t):
        n = next_int()
        a = [0] * n
        p = 0
        for i in range(n):
            x = next_int()
            a[i] = x
            p += x

        if p == 0:
            out.append("1")
            continue

        cap = 2 * n + 10
        F = array('q', [0]) * cap
        G = array('q', [0]) * cap
        L = array('q', [0]) * cap

        head = n + 3
        tail = head + 1

        F[head] = 0
        G[head] = 1
        L[head] = 1

        F[tail] = 1
        G[tail] = 1
        L[tail] = p

        l = 0
        r = 0
        v = 0
        gv = 1
        gz = p % MOD
        tv = 0
        tz = 0

        for ai in a:
            if ai >= 0:
                ls = ai
                while ls > 0:
                    f = F[tail]
                    g = G[tail]
                    length = L[tail]
                    tail -= 1

                    if ls < length:
                        tail += 1
                        F[tail] = f
                        G[tail] = g
                        L[tail] = length - ls
                        length = ls

                    sub = g * (length % MOD) % MOD
                    if f == v:
                        gv = (gv - sub) % MOD
                    else:
                        gz = (gz - sub) % MOD
                    ls -= length

                l += ai
                rp = r + ai
                r = rp if rp < p else p

                if l > r:
                    v += 1
                    l = ai
                    r = p
                    gv = gz
                    tv = tz
                    gz = 0
                    tz = 0

                gz = (gz - tz * (ai % MOD)) % MOD

                if ai > 0:
                    head -= 1
                    F[head] = v + 1
                    G[head] = (-tz) % MOD
                    L[head] = ai

                tz = (tz + gv + tv * ((r - l + 1) % MOD)) % MOD

            else:
                x = -ai
                ls = x
                while ls > 0:
                    f = F[head]
                    g = G[head]
                    length = L[head]
                    head += 1

                    if ls < length:
                        head -= 1
                        F[head] = f
                        G[head] = g
                        L[head] = length - ls
                        length = ls

                    sub = g * (length % MOD) % MOD
                    if f == v:
                        gv = (gv - sub) % MOD
                    else:
                        gz = (gz - sub) % MOD
                    ls -= length

                r -= x
                lm = l - x
                l = lm if lm > 0 else 0

                if l > r:
                    v += 1
                    l = 0
                    r = p - x
                    gv = gz
                    tv = tz
                    gz = 0
                    tz = 0

                gz = (gz - tz * (x % MOD)) % MOD

                tail += 1
                F[tail] = v + 1
                G[tail] = (-tz) % MOD
                L[tail] = x

                tz = (tz + gv + tv * ((r - l + 1) % MOD)) % MOD

        ans = (G[tail] + (tv if r == p else tz)) % MOD
        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
