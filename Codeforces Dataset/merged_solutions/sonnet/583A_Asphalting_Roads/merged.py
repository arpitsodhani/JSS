import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    plan = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n * n)]
    return n, plan

# Clause working_days [Confidence: 0.80]
def working_days(n, plan):
    rows = [False] * (n + 1)
    columns = [False] * (n + 1)
    days = []
    for i in range(len(plan)):
        entry_row, column = plan[i]
        if rows[entry_row] or columns[column]:
            continue
        rows[entry_row] = True
        columns[column] = True
        days.append(i + 1)
    return days

# Clause main [Confidence: 1.00]
def main():
    n, plan = read_input()
    sys.stdout.write(" ".join(map(str, working_days(n, plan))) + "\n")


if __name__ == "__main__":
    main()

