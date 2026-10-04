# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def decide(flat_rows):
    for i in range(0, len(flat_rows), 8):
        if "RRRRRRRR" in flat_rows[i:i + 8]:
            yield "R"
        else:
            yield "B"

# CLAUSE: finish_program
tokens = sys.stdin.read().split()
case_count = int(tokens[0])
rows = tokens[1:1 + case_count * 8]
sys.stdout.write("\n".join(decide(rows)))
