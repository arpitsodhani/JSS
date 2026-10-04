# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 1000000007


# Clause solve_logic [Confidence: 1.00]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = values[pos]
    pos += 1
    cases = []
    largest = 0

    for _ in range(t):
        n = values[pos]
        k = values[pos + 1]
        pos += 2
        cnt_one = sum(values[pos:pos + n])
        pos += n
        cases.append((n, k, cnt_one))
        if n > largest:
            largest = n

    fact = [1] * (largest + 1)
    for x in range(2, largest + 1):
        fact[x] = fact[x - 1] * x % MOD

    inv_fact = [1] * (largest + 1)
    inv_fact[largest] = pow(fact[largest], MOD - 2, MOD)
    for x in range(largest, 0, -1):
        inv_fact[x - 1] = inv_fact[x] * x % MOD

    def choose(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

    out = []
    for n, k, cnt_one in cases:
        cnt_zero = n - cnt_one
        low = k // 2 + 1
        ans = 0
        for picked_one in range(low, k + 1):
            ans = (ans + choose(cnt_one, picked_one) * choose(cnt_zero, k - picked_one)) % MOD
        out.append(str(ans))

    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


