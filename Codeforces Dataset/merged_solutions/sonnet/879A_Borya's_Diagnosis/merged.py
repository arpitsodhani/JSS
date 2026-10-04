# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    day = 0
    pos = 1
    for _ in range(n):
        start = values[pos]
        step = values[pos + 1]
        pos += 2
        if day < start:
            day = start
        else:
            day = start + ((day - start) // step + 1) * step
    print(day)


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


