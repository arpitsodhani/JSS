# CLAUSE: setup_environment
import sys

MOD = 10**9 + 7

def build_factorials(limit):
    fact = [1] * (limit + 1)
    inv_fact = [1] * (limit + 1)
    for i in range(2, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return fact, inv_fact

def choose(n, k, fact, inv_fact):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

# CLAUSE: solve_logic
def solve_case(n, l, r, fact, inv_fact):
    left_extra = 1 - l
    right_extra = r - n
    low = n // 2
    high = n - low
    common = min(left_extra, right_extra)

    ways = choose(n, low, fact, inv_fact)
    if low != high:
        ways = ways * 2 % MOD

    answer = common % MOD * ways % MOD

    for shift in range(common + 1, common + high + 1):
        forced_left = max(0, shift - left_extra)
        forced_right = max(0, shift - right_extra)
        free = n - forced_left - forced_right
        if free >= 0:
            answer += choose(free, low - forced_left, fact, inv_fact)
            if low != high:
                answer += choose(free, high - forced_left, fact, inv_fact)
            answer %= MOD

    return answer

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    tests = []
    max_n = 0
    at = 1
    for _ in range(t):
        n, l, r = data[at], data[at + 1], data[at + 2]
        at += 3
        tests.append((n, l, r))
        if n > max_n:
            max_n = n

    fact, inv_fact = build_factorials(max_n)
    out = [str(solve_case(n, l, r, fact, inv_fact)) for n, l, r in tests]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
