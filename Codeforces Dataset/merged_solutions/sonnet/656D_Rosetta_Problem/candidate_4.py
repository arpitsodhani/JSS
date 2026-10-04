# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
tokens = sys.stdin.read().strip()
values = [1 for character in tokens if character == "1"]
result = sum(values)

# CLAUSE: finish_program
print(result)
