# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def count_row_ones(row):
    total = 0
    for ch in row:
        total += ch == "1"
    return total

def main():
    lines = sys.stdin.read().splitlines()
    q = int(lines[0])
    line = 1
    answers = []

    for _ in range(q):
        while lines[line] == "":
            line += 1
        n, m = map(int, lines[line].split())
        line += 1

        column_counts = [0] * m
        bad_rows = 0

        for _ in range(n):
            row = lines[line].strip()
            line += 1

            if count_row_ones(row) % 2:
                bad_rows += 1

            for index, digit in enumerate(row):
                if digit == "1":
                    column_counts[index] += 1

        bad_columns = 0
        for total in column_counts:
            bad_columns += total % 2

        answers.append(str(max(bad_rows, bad_columns)))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
main()
