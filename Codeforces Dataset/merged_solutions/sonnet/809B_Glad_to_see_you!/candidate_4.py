# CLAUSE: setup_environment
import sys

def say(kind, x, y):
    print(kind, x, y, flush=True)

def confirmed(x, y):
    say(1, x, y)
    reply = sys.stdin.readline().strip()
    return reply == "TAK"

# CLAUSE: solve_logic
def search_segment(bounds):
    left, right = bounds
    while True:
        if left == right:
            return left
        middle = (left + right) >> 1
        if confirmed(middle, middle + 1):
            right = middle
        else:
            left = middle + 1

def solve_case():
    tokens = sys.stdin.readline().split()
    if not tokens:
        return
    n = int(tokens[0])
    first = search_segment((1, n))
    second = None
    ranges = []
    if first > 1:
        ranges.append((1, first - 1, True))
    if first < n:
        ranges.append((first + 1, n, False))
    for left, right, needs_check in ranges:
        found = search_segment((left, right))
        if not needs_check or confirmed(found, first):
            second = found
            break
    say(2, first, second)

# CLAUSE: finish_program
if __name__ == "__main__":
    solve_case()
