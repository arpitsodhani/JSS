# CLAUSE: setup_environment
import sys
from functools import lru_cache

MOD = 676767677

def build_combinations(size):
    factorials = [1] * size
    for x in range(2, size):
        factorials[x] = factorials[x - 1] * x % MOD

    inverse_factorials = [1] * size
    inverse_factorials[size - 1] = pow(factorials[size - 1], MOD - 2, MOD)
    x = size - 1
    while x:
        inverse_factorials[x - 1] = inverse_factorials[x] * x % MOD
        x -= 1

    def choose(n, k):
        if n < 0 or k < 0 or k > n:
            return 0
        return factorials[n] * inverse_factorials[k] % MOD * inverse_factorials[n - k] % MOD

    return choose

def main():
    tokens = sys.stdin.buffer.read().split()
    test_count = int(tokens[0])
    tests = [(int(tokens[i]), int(tokens[i + 1])) for i in range(1, 2 * test_count, 2)]
    max_size = max((n + m + 5 for n, m in tests), default=5)
    choose = build_combinations(max_size)

    def monotone_count(length, lower, upper):
        if lower > upper:
            return 0
        return choose(upper - lower + length, length)

# CLAUSE: solve_logic
    out = []
    for n, m in tests:
        @lru_cache(maxsize=None)
        def dp(left, right, lower, upper):
            if left > right or lower > upper:
                return 0, 0
            if left == right:
                base = upper - lower + 1
                return base % MOD, base % MOD

            middle = (left + right) >> 1
            left_width = middle - left
            right_width = right - middle
            score_sum = 0
            found_sum = 0

            value = lower
            while value <= upper:
                lc = monotone_count(left_width, lower, value)
                rc = monotone_count(right_width, value, upper)

                direct = lc * rc % MOD
                score_sum += direct
                found_sum += direct

                if left_width and lower < value:
                    sub_score, sub_found = dp(left, middle - 1, lower, value - 1)
                    score_sum += rc * (sub_score + sub_found)
                    found_sum += rc * sub_found

                if right_width and value < upper:
                    sub_score, sub_found = dp(middle + 1, right, value + 1, upper)
                    score_sum += lc * (sub_score + sub_found)
                    found_sum += lc * sub_found

                score_sum %= MOD
                found_sum %= MOD
                value += 1

            return score_sum, found_sum

        answer, unused = dp(1, n, 1, m)
        out.append(str(answer))

# CLAUSE: finish_program
    print("\n".join(out))

if __name__ == "__main__":
    main()
