# CLAUSE: setup_environment
import sys

MOD = 998244353

def make_row(k):
    values = [0] * (k + 1)
    values[0] = 1
    for taken in range(1, k + 1):
        next_values = values[:]
        next_values[0] = 0
        for parts in range(1, taken + 1):
            next_values[parts] = (values[parts - 1] + parts * values[parts]) % MOD
        values = next_values
    return values

def falling_sum(n, m_mod, odd_mod, k, stir):
    limit = k if k < n else n
    inverse = pow(m_mod, MOD - 2, MOD)
    m_part = pow(m_mod, n, MOD)
    n_part = 1
    odd_part = 1
    total = 0

    for groups, s_value in enumerate(stir[:limit + 1]):
        term = s_value * n_part % MOD
        term = term * odd_part % MOD
        total = (total + term * m_part) % MOD
        n_part = n_part * ((n - groups) % MOD) % MOD
        odd_part = odd_part * odd_mod % MOD
        m_part = m_part * inverse % MOD

    return total

# CLAUSE: solve_logic
def compute(n, m, k):
    m_mod = m % MOD
    if k == 0:
        return pow(m_mod, n, MOD)

    odd_mod = ((m + 1) // 2) % MOD
    stir = make_row(k)

    if m_mod:
        return falling_sum(n, m_mod, odd_mod, k, stir)

    if n > k:
        return 0

    product = 1
    for x in range(1, n + 1):
        product = product * x % MOD * odd_mod % MOD
    return stir[n] * product % MOD

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    t = int(raw[0])
    result = [""] * t
    p = 1
    for case_id in range(t):
        n = int(raw[p])
        m = int(raw[p + 1])
        k = int(raw[p + 2])
        p += 3
        result[case_id] = str(compute(n, m, k))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
