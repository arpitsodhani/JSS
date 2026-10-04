# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def build_combinations(limit):
    factorial = [1] * (limit + 1)
    inverse_factorial = [1] * (limit + 1)

    for i in range(1, limit + 1):
        factorial[i] = factorial[i - 1] * i % MOD

    inverse_factorial[limit] = pow(factorial[limit], MOD - 2, MOD)
    i = limit
    while i:
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD
        i -= 1

    def combination(n, r):
        return 0 if r < 0 or r > n else factorial[n] * inverse_factorial[r] % MOD * inverse_factorial[n - r] % MOD

    return combination

def main():
    raw = tuple(map(int, sys.stdin.buffer.read().split()))
    count_tests = raw[0]
    pointer = 1
    tests = []
    max_len = 0

    for _ in range(count_tests):
        n = raw[pointer]
        k = raw[pointer + 1]
        pointer += 2
        ones = 0
        end = pointer + n
        while pointer < end:
            ones += raw[pointer]
            pointer += 1
        tests.append((k, ones, n - ones))
        max_len = max(max_len, n)

    comb = build_combinations(max_len)
    result_lines = []

    for k, ones, zeros in tests:
        need = k // 2 + 1
        total = 0
        upper = min(k, ones)
        lower = max(need, k - zeros)
        for x in range(lower, upper + 1):
            total += comb(ones, x) * comb(zeros, k - x)
            if total >= MOD:
                total %= MOD
        result_lines.append(str(total % MOD))

    print("\n".join(result_lines))

# CLAUSE: finish_program
main()
