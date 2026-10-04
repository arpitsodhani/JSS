# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
tokens = sys.stdin.readline
count_line = tokens().strip()
answers = []
if count_line:
    for _ in range(int(count_line)):
        n = int(tokens())
        angle = math.pi / n / 2.0
        answers.append(f"{math.cos(angle) / math.sin(angle):.9f}")

# CLAUSE: finish_program
sys.stdout.write("\n".join(answers))
