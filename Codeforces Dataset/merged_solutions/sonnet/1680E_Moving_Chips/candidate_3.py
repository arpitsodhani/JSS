# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def column_mask(top, bottom, index):
    mask = 0
    if top[index] == "*":
        mask += 1
    if bottom[index] == "*":
        mask += 2
    return mask

def solve_case(n, top, bottom):
    occupied = [i for i in range(n) if top[i] == "*" or bottom[i] == "*"]
    left = occupied[0]
    right = occupied[-1]

    start = column_mask(top, bottom, left)
    upper = 1 if start & 2 else 0
    lower = 1 if start & 1 else 0

    for index in range(left + 1, right + 1):
        mask = column_mask(top, bottom, index)

        upper_extra = 1 if mask & 2 else 0
        lower_extra = 1 if mask & 1 else 0

        new_upper = min(upper + 1 + upper_extra, lower + 2 - upper_extra)
        new_lower = min(lower + 1 + lower_extra, upper + 2 - lower_extra)

        upper, lower = new_upper, new_lower

    return min(upper, lower)

def main():
    tokens = sys.stdin.read().split()
    total = int(tokens[0])
    answer = []
    at = 1
    for _ in range(total):
        n = int(tokens[at])
        top = tokens[at + 1]
        bottom = tokens[at + 2]
        at += 3
        answer.append(str(solve_case(n, top, bottom)))
    print("\n".join(answer))

# CLAUSE: finish_program
main()
