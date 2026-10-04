# CLAUSE: setup_environment
import sys
from math import comb

# CLAUSE: solve_logic
def main():
    original, received = sys.stdin.read().split()
    target = original.count("+") - original.count("-")
    known = received.count("+") - received.count("-")
    unknown = received.count("?")
    need = target - known

    if abs(need) > unknown or (need + unknown) % 2:
        answer = 0.0
    else:
        plus_count = (need + unknown) // 2
        answer = comb(unknown, plus_count) / (1 << unknown)

    print(f"{answer:.12f}")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
