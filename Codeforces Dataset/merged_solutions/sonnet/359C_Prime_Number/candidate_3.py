# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def answer(n, x, values):
    total = sum(values)
    exponents = sorted(total - value for value in values)
    i = 0
    carry = 0
    current = 0
    started = False

    while i < n:
        exponent = exponents[i]

        if started:
            while carry and current < exponent:
                if carry % x:
                    return pow(x, min(current, total), MOD)
                carry //= x
                current += 1
        else:
            started = True
            current = exponent

        same = 0
        while i < n and exponents[i] == exponent:
            same += 1
            i += 1

        current = exponent
        carry += same

        if carry % x:
            return pow(x, min(current, total), MOD)

        carry //= x
        current += 1

    while carry:
        if carry % x:
            return pow(x, min(current, total), MOD)
        carry //= x
        current += 1

    return pow(x, total, MOD)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    values = data[2:2 + n]
    sys.stdout.write(str(answer(n, x, values)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
