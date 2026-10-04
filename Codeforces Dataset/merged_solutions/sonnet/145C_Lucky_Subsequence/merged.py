# Clause setup_environment [Confidence: 0.40]
import sys

MOD = 1000000007

LUCKY = set()
frontier = [4, 7]
while frontier:
    value = frontier.pop()
    if value > 10000000000:
        continue
    LUCKY.add(value)
    frontier.append(value * 10 + 4)
    frontier.append(value * 10 + 7)


# Clause solve_logic [Confidence: 0.80]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    k = values[1]
    lucky = {}
    other = 0

    for x in values[2:]:
        if lucky_value(x):
            lucky[x] = lucky.get(x, 0) + 1
        else:
            other += 1

    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def choose(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

    dp = [0] * (len(lucky) + 1)
    dp[0] = 1
    limit = 0
    for count in lucky.values():
        for take in range(limit, -1, -1):
            dp[take + 1] = (dp[take + 1] + dp[take] * count) % MOD
        limit += 1

    total = 0
    for take_lucky in range(min(k, len(lucky)) + 1):
        total = (total + dp[take_lucky] * choose(other, k - take_lucky)) % MOD
    sys.stdout.write(str(total))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


