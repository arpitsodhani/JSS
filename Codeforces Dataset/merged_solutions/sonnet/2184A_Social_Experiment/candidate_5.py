# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def value(n):
    blocked = {0}
    if n == 1:
        return 1
    return 0 if n % 2 in blocked or n % 3 in blocked else 1

def main():
    items = list(map(int, sys.stdin.read().split()))
    if len(items) == 0:
        return
    print(value(items[0]))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
