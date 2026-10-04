# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
