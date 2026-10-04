# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    lines = sys.stdin.read().split()
    total = int(lines[0])
    out = []
    start = 1
    for case_index in range(total):
        stop = start + 8
        found = False
        row_index = start
        while row_index < stop:
            if set(lines[row_index]) == {"R"}:
                found = True
            row_index += 1
        out.append("R" if found else "B")
        start = stop

# CLAUSE: finish_program
    print(*out, sep="\n")

main()
