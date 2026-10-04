# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if len(data) >= 2:
    s = data[1]
else:
    s = data[0] if data else ""

print("".join(str(len(part)) for part in s.split("0")))

# CLAUSE: finish_program
RESULT_SENTINEL = None
