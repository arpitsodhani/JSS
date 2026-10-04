# CLAUSE: setup_environment
import sys

ZERO = {"zero", "|0>", "0"}
PLUS = {"plus", "|+>", "+", "1"}

# CLAUSE: solve_logic
def classify(word):
    item = word.strip().lower()
    if item in ZERO:
        return "0"
    if item in PLUS:
        return "1"
    return "-1"

def main():
    tokens = sys.stdin.read().split()
    if tokens:
        sys.stdout.write("\n".join(classify(token) for token in tokens))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
