# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_number(n):
    if n == 1:
        return "9"
    digits = ["9", "8"]
    current = 9
    for _ in range(n - 2):
        digits.append(str(current))
        current = (current + 1) % 10
    return "".join(digits)

def main():
    values = list(map(int, sys.stdin.read().split()))
    t = values[0]
    answers = [build_number(values[i]) for i in range(1, t + 1)]

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
