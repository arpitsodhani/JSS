# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    zero_names = ("zero", "|0>", "0")
    plus_names = ("plus", "|+>", "+", "1")
    pieces = sys.stdin.read().split()
    lines = [None] * len(pieces)
    index = 0
    while index < len(pieces):
        current = pieces[index].strip().lower()
        if current in zero_names:
            lines[index] = "0"
        elif current in plus_names:
            lines[index] = "1"
        else:
            lines[index] = "-1"
        index += 1
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
