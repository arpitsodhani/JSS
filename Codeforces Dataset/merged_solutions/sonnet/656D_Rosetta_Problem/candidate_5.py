# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve(source):
    cleaned = source.strip()
    return len(cleaned.split("1")) - 1

# CLAUSE: finish_program
print(solve(sys.stdin.read()))
