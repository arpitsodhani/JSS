# CLAUSE: setup_environment
from sys import stdin, stdout

# CLAUSE: solve_logic
def step_size(number, digits):
    top = max(digits)
    if top < 9:
        return top, 1
    pos = len(digits) - 1
    while digits[pos] != "9":
        pos -= 1
    zeros = len(digits) - pos - 1
    base = 10 ** zeros
    return 9, number % base // 9 + 1

def main():
    current = int(stdin.buffer.readline())
    result = 0
    while current > 0:
        d, repeat = step_size(current, str(current))
        current -= d * repeat
        result += repeat

# CLAUSE: finish_program
    stdout.write(str(result))

if __name__ == "__main__":
    main()
