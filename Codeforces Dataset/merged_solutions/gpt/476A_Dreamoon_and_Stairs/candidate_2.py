# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().strip().split()
    n, m = map(int, data[:2])
    low = (n + 1) // 2
    moves = (low + m - 1) // m * m
    print(moves if moves <= n else -1)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
