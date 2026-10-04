# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    if n == 1:
        ans = 1
    elif n % 2 == 0 or n % 3 == 0:
        ans = 0
    else:
        ans = 1
    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
