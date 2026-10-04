# CLAUSE: setup_environment
import sys

MOD = 998244353

def stirling_row_for_power(power):
    row = [1] + [0] * power
    for value in range(1, power + 1):
        for count in range(value, 0, -1):
            row[count] = (row[count - 1] + row[count] * count) % MOD
        row[0] = 0
    return row

def divisible_m_case(n, k, odd, row):
    if n > k:
        return 0
    value = row[n]
    for multiplier in range(1, n + 1):
        value = value * multiplier % MOD
        value = value * odd % MOD
    return value

def regular_case(n, k, odd, m_mod, row):
    last = min(n, k)
    inv = pow(m_mod, MOD - 2, MOD)
    powers = [1] * (last + 1)
    current = pow(m_mod, n, MOD)
    for i in range(last + 1):
        powers[i] = current
        current = current * inv % MOD

    answer = 0
    falling = 1
    odd_power = 1
    for i in range(last + 1):
        answer = (answer + row[i] * falling % MOD * odd_power % MOD * powers[i]) % MOD
        falling = falling * ((n - i) % MOD) % MOD
        odd_power = odd_power * odd % MOD
    return answer

# CLAUSE: solve_logic
def solve_case(n, m, k):
    reduced_m = m % MOD
    if k == 0:
        return pow(reduced_m, n, MOD)

    odd = ((m + 1) // 2) % MOD
    row = stirling_row_for_power(k)

    if reduced_m == 0:
        return divisible_m_case(n, k, odd, row)
    return regular_case(n, k, odd, reduced_m, row)

# CLAUSE: finish_program
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    answers = []
    cursor = 1
    for _ in range(t):
        answers.append(str(solve_case(numbers[cursor], numbers[cursor + 1], numbers[cursor + 2])))
        cursor += 3
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
