# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, rows):
    masks = [
        (1 if rows[0][i] == "*" else 0) | (2 if rows[1][i] == "*" else 0)
        for i in range(n)
    ]

    active = [i for i, mask in enumerate(masks) if mask]
    begin = active[0]
    end = active[-1]

    costs = {
        0: 1 if masks[begin] & 2 else 0,
        1: 1 if masks[begin] & 1 else 0,
    }

    index = begin + 1
    while index <= end:
        mask = masks[index]
        updated = {}
        for row in (0, 1):
            opposite_bit = 2 if row == 0 else 1
            vertical = 1 if mask & opposite_bit else 0
            updated[row] = min(
                costs[row] + 1 + vertical,
                costs[1 - row] + 2 - vertical,
            )
        costs = updated
        index += 1

    return min(costs.values())

def main():
    parts = sys.stdin.read().split()
    cases = int(parts[0])
    result = []
    cursor = 1
    for _ in range(cases):
        n = int(parts[cursor])
        rows = (parts[cursor + 1], parts[cursor + 2])
        cursor += 3
        result.append(str(solve_case(n, rows)))
    sys.stdout.write("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
