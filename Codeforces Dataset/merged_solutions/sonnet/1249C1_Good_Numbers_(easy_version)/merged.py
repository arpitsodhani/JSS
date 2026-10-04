# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.67]
def next_good(n):
    digits = []
    while n:
        digits.append(n % 3)
        n //= 3
    digits.append(0)

    last_two = -1
    for i in range(len(digits)):
        if digits[i] == 2:
            last_two = i

    if last_two < 0:
        value = 0
        power = 1
        for digit in digits:
            value += digit * power
            power *= 3
        return value

    j = last_two + 1
    while digits[j] == 1:
        digits[j] = 0
        j += 1
    digits[j] = 1

    for i in range(j):
        digits[i] = 0

    value = 0
    power = 1
    for digit in digits:
        value += digit * power
        power *= 3
    return value

def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = []
    for i in range(q):
        out.append(str(next_good(int(data[i + 1]))))
    sys.stdout.write("\n".join(out))


# Clause finish_program [Confidence: 0.67]
if __name__ == "__main__":
    main()


