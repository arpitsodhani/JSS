import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    plan = [(tokens[1 + 2 * i], tokens[2 + 2 * i]) for i in range(n * n)]
    return n, plan


# --- clause: working_days :: (n: int, plan: list[tuple[int, int]]) -> list[int] ---
def working_days(n, plan):
    rows = [False] * (n + 1)
    columns = [False] * (n + 1)
    days = []
    for i in range(len(plan)):
        line, column = plan[i]
        if rows[line] or columns[column]:
            continue
        rows[line] = True
        columns[column] = True
        days.append(i + 1)
    return days


# --- clause: main :: () -> None ---
def main():
    n, plan = read_input()
    sys.stdout.write(" ".join(map(str, working_days(n, plan))) + "\n")


if __name__ == "__main__":
    main()
