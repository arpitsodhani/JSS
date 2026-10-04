import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    plan = [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(n * n)]
    return n, plan


# --- clause: working_days :: (n: int, plan: list[tuple[int, int]]) -> list[int] ---
def working_days(n, plan):
    busy = set()
    days = []
    day = 0
    for row, column in plan:
        day += 1
        if ("r", row) in busy or ("c", column) in busy:
            continue
        busy.add(("r", row))
        busy.add(("c", column))
        days.append(day)
    return days


# --- clause: main :: () -> None ---
def main():
    n, plan = read_input()
    sys.stdout.write(" ".join(map(str, working_days(n, plan))) + "\n")


if __name__ == "__main__":
    main()
