# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def valid_fraction(data):
    p = data[0]
    q = data[1]
    n = data[2]
    seq = data[3:]

    for index, wanted in zip(range(n), seq):
        if q == 0:
            return False

        whole = p // q
        remainder = p - whole * q

        if whole != wanted:
            return False

        final_term = index == n - 1
        if final_term:
            return remainder == 0

        if remainder == 0:
            return False

        p = q
        q = remainder

    return False


def main():
    data = tuple(map(int, sys.stdin.buffer.read().split()))
    sys.stdout.write("YES" if valid_fraction(data) else "NO")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
