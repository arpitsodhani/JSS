# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    parts = sys.stdin.readline().split()
    if not parts:
        return
    n = int(parts[0])
    answer = int(n == 1 or (n % 2 != 0 and n % 3 != 0))
    sys.stdout.write(f"{answer}\n")

# CLAUSE: finish_program
main()
