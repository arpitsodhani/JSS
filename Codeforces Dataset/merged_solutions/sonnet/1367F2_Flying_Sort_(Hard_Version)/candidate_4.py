# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def minimum_moves(values):
    ordered = sorted(values)
    rank_stacks = {}
    for rank in range(len(ordered) - 1, -1, -1):
        value = ordered[rank]
        if value in rank_stacks:
            rank_stacks[value].append(rank)
        else:
            rank_stacks[value] = [rank]

    where = [0] * len(values)
    for index, value in enumerate(values):
        where[rank_stacks[value].pop()] = index

    keep = 0
    current = 0
    previous = -1
    for index in where:
        current = current + 1 if previous < index else 1
        keep = keep if keep > current else current
        previous = index
    return len(values) - keep

def parse_and_solve():
    items = sys.stdin.buffer.read().split()
    cases = int(items[0])
    pointer = 1
    answers = []
    for _ in range(cases):
        n = int(items[pointer])
        pointer += 1
        values = tuple(int(x) for x in items[pointer:pointer + n])
        pointer += n
        answers.append(str(minimum_moves(values)))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    parse_and_solve()
