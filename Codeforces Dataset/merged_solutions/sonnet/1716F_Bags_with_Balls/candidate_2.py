# CLAUSE: setup_environment
import sys

MOD = 998244353

def build_stirling(k):
    row = [0] * (k + 1)
    row[0] = 1
    for x in range(1, k + 1):
        j = x
        while j:
            row[j] = (row[j - 1] + row[j] * j) % MOD
            j -= 1
        row[0] = 0
    return row

# CLAUSE: solve_logic
def solve_one(n, m, k):
    if k == 0:
        return pow(m % MOD, n, MOD)

    odd = ((m + 1) // 2) % MOD
    mm = m % MOD
    stir = build_stirling(k)

    if mm == 0:
        if n > k:
            return 0
        fact = 1
        p = 1
        for v in range(1, n + 1):
            fact = fact * v % MOD
            p = p * odd % MOD
        return stir[n] * fact % MOD * p % MOD

    upto = min(k, n)
    inv_m = pow(mm, MOD - 2, MOD)
    ways = pow(mm, n, MOD)
    falling = 1
    odd_pow = 1
    ans = 0

    for i in range(upto + 1):
        ans = (ans + stir[i] * falling % MOD * odd_pow % MOD * ways) % MOD
        if i != upto:
            falling = falling * ((n - i) % MOD) % MOD
            odd_pow = odd_pow * odd % MOD
            ways = ways * inv_m % MOD

    return ans

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        out.append(str(solve_one(n, m, k)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
