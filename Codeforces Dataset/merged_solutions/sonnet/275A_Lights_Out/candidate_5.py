# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    answer = []

    for r in range(3):
        line = []
        for c in range(3):
            parity = 0
            for nr, nc in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < 3 and 0 <= nc < 3:
                    parity ^= numbers[nr * 3 + nc] & 1
            line.append("0" if parity else "1")
        answer.append("".join(line))

    print("\n".join(answer))

# CLAUSE: finish_program
main()
