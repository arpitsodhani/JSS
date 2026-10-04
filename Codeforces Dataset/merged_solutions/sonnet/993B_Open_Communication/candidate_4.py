# CLAUSE: setup_environment
import sys

def read_pairs(values, count, start):
    pairs = []
    for offset in range(start, start + 2 * count, 2):
        pairs.append(frozenset((values[offset], values[offset + 1])))
    return pairs, start + 2 * count

def relation_values(group_a, group_b):
    rows = []
    all_seen = set()
    for item in group_a:
        row = set()
        for other in group_b:
            common = item & other
            if len(common) == 1:
                value = next(iter(common))
                row.add(value)
                all_seen.add(value)
        rows.append(row)
    return rows, all_seen

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.read().split()))
    n = values[0]
    m = values[1]
    first, index = read_pairs(values, n, 2)
    second, index = read_pairs(values, m, index)

    left_rows, all_answers = relation_values(first, second)

    if len(all_answers) == 1:
        print(all_answers.pop())
        return

    for row in left_rows:
        if len(row) > 1:
            print(-1)
            return

    right_rows, unused = relation_values(second, first)
    for row in right_rows:
        if len(row) > 1:
            print(-1)
            return

    print(0)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
