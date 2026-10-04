# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    table = {
        "zero": 0,
        "|0>": 0,
        "0": 0,
        "plus": 1,
        "|+>": 1,
        "+": 1,
        "1": 1,
    }
    data = sys.stdin.read().split()
    answers = []
    for token in data:
        key = token.strip().lower()
        answers.append(str(table.get(key, -1)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
