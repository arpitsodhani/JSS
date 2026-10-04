# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    digits = list(sys.stdin.readline().strip())
    last_digit = ord(digits[-1]) - 48
    chosen = -1

    for index in range(len(digits) - 1):
        value = ord(digits[index]) - 48
        if value % 2 == 0:
            chosen = index
            if value < last_digit:
                break

    if chosen < 0:
        sys.stdout.write("-1\n")
    else:
        digits[chosen], digits[-1] = digits[-1], digits[chosen]
        sys.stdout.write("".join(digits) + "\n")


# Clause finish_program [Confidence: 0.80]
main()


