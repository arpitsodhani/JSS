# CLAUSE: setup_environment
import sys
from itertools import product

# CLAUSE: solve_logic
def main():
    source, message = sys.stdin.read().split()
    target = 0
    for command in source:
        target += 1 if command == "+" else -1

    base = 0
    missing = 0
    for command in message:
        if command == "+":
            base += 1
        elif command == "-":
            base -= 1
        else:
            missing += 1

    success = 0
    total = 0
    for choices in product((1, -1), repeat=missing):
        total += 1
        if base + sum(choices) == target:
            success += 1

    print("{:.12f}".format(success / total))

# CLAUSE: finish_program
main()
