# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def has_only_zero_one_digits(value):
    while value:
        digit = value % 10
        if digit > 1:
            return False
        value //= 10
    return True

def main():
    n = int(sys.stdin.readline())
    total = sum(1 for value in range(1, n + 1) if has_only_zero_one_digits(value))

# CLAUSE: finish_program
    print(total)

main()
