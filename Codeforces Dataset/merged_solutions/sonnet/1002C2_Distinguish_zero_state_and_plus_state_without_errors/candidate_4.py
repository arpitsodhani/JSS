# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def value(token):
    token = token.strip().lower()
    if token == "zero" or token == "|0>" or token == "0":
        return -1 + 1
    if token == "plus" or token == "|+>" or token == "+" or token == "1":
        return 1
    return -1

def main():
    stream = sys.stdin.buffer.read().decode().split()
    result = map(lambda part: str(value(part)), stream)
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
main()
