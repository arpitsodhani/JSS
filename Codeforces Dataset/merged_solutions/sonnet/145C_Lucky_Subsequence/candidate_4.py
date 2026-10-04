# CLAUSE: setup_environment
import sys

MOD = 1000000007

def is_lucky_number(text):
    return text and all(ch == "4" or ch == "7" for ch in text)

def prepare_factorials(size):
    factorial = [1] * (size + 1)
    inverse_factorial = [1] * (size + 1)
    for value in range(2, size + 1):
        factorial[value] = factorial[value - 1] * value % MOD
    inverse_factorial[size] = pow(factorial[size], MOD - 2, MOD)
    value = size
    while value:
        inverse_factorial[value - 1] = inverse_factorial[value] * value % MOD
        value -= 1
    return factorial, inverse_factorial

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    k = int(tokens[1])

    groups = {}
    ordinary = 0
    for item in tokens[2:]:
        number = int(item)
        if is_lucky_number(item.decode()):
            groups[number] = groups.get(number, 0) + 1
        else:
            ordinary += 1

    fact, inv_fact = prepare_factorials(n)

    def c(total, chosen):
        if chosen < 0 or chosen > total:
            return 0
        return fact[total] * inv_fact[chosen] % MOD * inv_fact[total - chosen] % MOD

    polynomial = [1]
    for frequency in groups.values():
        polynomial.append(0)
        index = len(polynomial) - 2
        while index >= 0:
            polynomial[index + 1] = (polynomial[index + 1] + polynomial[index] * frequency) % MOD
            index -= 1

    answer = 0
    upper = min(k, len(groups))
    for used_lucky in range(upper + 1):
        answer += polynomial[used_lucky] * c(ordinary, k - used_lucky)
        answer %= MOD

    sys.stdout.write(f"{answer}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
