# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def count_ones(text):
    total = 0
    for ch in text.strip():
        if ch == "1":
            total += 1
    return total

# CLAUSE: finish_program
sys.stdout.write(str(count_ones(sys.stdin.read())) + "\n")
