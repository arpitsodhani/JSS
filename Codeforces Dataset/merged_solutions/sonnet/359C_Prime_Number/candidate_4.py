# CLAUSE: setup_environment
import sys

MOD = 1000000007

# CLAUSE: solve_logic
def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    n = items[0]
    x = items[1]
    values = items[2:2 + n]
    total = sum(values)

    groups = {}
    for value in values:
        exponent = total - value
        groups[exponent] = groups.get(exponent, 0) + 1

    carry = 0
    position = None
    result_exp = total

    for exponent in sorted(groups):
        if position is not None:
            while carry and position < exponent:
                quotient, remainder = divmod(carry, x)
                if remainder:
                    result_exp = min(position, total)
                    break
                carry = quotient
                position += 1
            if result_exp != total:
                break

        position = exponent
        carry += groups[exponent]
        quotient, remainder = divmod(carry, x)
        if remainder:
            result_exp = min(position, total)
            break
        carry = quotient
        position += 1
    else:
        while carry:
            quotient, remainder = divmod(carry, x)
            if remainder:
                result_exp = min(position, total)
                break
            carry = quotient
            position += 1

    print(pow(x, result_exp, MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
