# CLAUSE: setup_environment
import sys

MOD = 998244353

def stirling_numbers_second_kind(k):
    previous = [1]
    for size in range(1, k + 1):
        current = [0] * (size + 1)
        for groups in range(1, size + 1):
            keep = previous[groups] * groups if groups < size else 0
            add = previous[groups - 1]
            current[groups] = (add + keep) % MOD
        previous = current
    return previous + [0] * (k + 1 - len(previous))

def zero_base_value(n, k, odd_count, stirling):
    if n > k:
        return 0
    factorial = 1
    odd_power = 1
    for number in range(1, n + 1):
        factorial = factorial * number % MOD
        odd_power = odd_power * odd_count % MOD
    return stirling[n] * factorial % MOD * odd_power % MOD

# CLAUSE: solve_logic
def answer_case(n, m, k):
    base = m % MOD
    if k == 0:
        return pow(base, n, MOD)

    odd_count = ((m + 1) // 2) % MOD
    stirling = stirling_numbers_second_kind(k)

    if base == 0:
        return zero_base_value(n, k, odd_count, stirling)

    limit = min(n, k)
    inverse_base = pow(base, MOD - 2, MOD)
    base_power = pow(base, n, MOD)

    result = 0
    falling_n = 1
    odd_factor = 1

    index = 0
    while index <= limit:
        result += stirling[index] * falling_n % MOD * odd_factor % MOD * base_power
        result %= MOD
        falling_n = falling_n * ((n - index) % MOD) % MOD
        odd_factor = odd_factor * odd_count % MOD
        base_power = base_power * inverse_base % MOD
        index += 1

    return result

# CLAUSE: finish_program
def main():
    values = tuple(map(int, sys.stdin.buffer.read().split()))
    total = values[0]
    answers = []
    offset = 1
    for case_index in range(total):
        n = values[offset]
        m = values[offset + 1]
        k = values[offset + 2]
        offset += 3
        answers.append(str(answer_case(n, m, k)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
