# CLAUSE: setup_environment
import sys

read_line = sys.stdin.readline

def ask(left, right):
    print(f"? {left} {right}")
    sys.stdout.flush()
    return int(read_line())

# CLAUSE: solve_logic
n = int(read_line())

def search(left, right):
    if left > right:
        return 0
    if left == right:
        return ask(left, right)
    middle = (left + right) // 2
    first = search(left, middle)
    second = search(middle + 1, right)
    return first if first >= second else second

answer = search(1, n)

# CLAUSE: finish_program
print(f"! {answer}")
sys.stdout.flush()
