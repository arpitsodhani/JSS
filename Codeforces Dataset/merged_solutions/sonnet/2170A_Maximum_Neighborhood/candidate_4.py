# CLAUSE: setup_environment
from sys import stdin, stdout

# CLAUSE: solve_logic
def main():
    data = stdin.buffer.read().split()
    if data:
        n = int(data[0])
        square = n * n
        candidates = [1] if n == 1 else [3 * square - n - 1]
        if n >= 3:
            candidates += [5 * (square - n - 1), 4 * (square - 1) - n]
        stdout.write(str(max(candidates)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
