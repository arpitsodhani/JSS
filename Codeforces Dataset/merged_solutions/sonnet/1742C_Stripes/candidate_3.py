# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def red_row_exists(rows):
    return any(row.count("R") == 8 for row in rows)

def solve(data):
    t = int(data[0])
    answers = []
    cursor = 1
    for _ in range(t):
        rows = data[cursor:cursor + 8]
        cursor += 8
        answers.append("R" if red_row_exists(rows) else "B")
    return answers

# CLAUSE: finish_program
items = sys.stdin.read().split()
sys.stdout.write("\n".join(solve(items)))
