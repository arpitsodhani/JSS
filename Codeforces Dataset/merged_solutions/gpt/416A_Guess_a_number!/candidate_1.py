# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    low = -10**18
    high = 10**18
    idx = 1

    for _ in range(n):
        op = data[idx]
        x = int(data[idx + 1])
        ans = data[idx + 2]
        idx += 3

        if ans == 'N':
            if op == '>':
                op = '<='
            elif op == '<':
                op = '>='
            elif op == '>=':
                op = '<'
            else:
                op = '>'

        if op == '>':
            low = max(low, x + 1)
        elif op == '>=':
            low = max(low, x)
        elif op == '<':
            high = min(high, x - 1)
        else:
            high = min(high, x)

    if low <= high:
        print(low)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
