import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    exams = []
    pos = 2
    for _ in range(m):
        exams.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return n, m, exams


# --- clause: build_schedule :: (n: int, m: int, exams: list[tuple[int, int, int]]) -> list[int] | None ---
def build_schedule(n, m, exams):
    plan = [0] * (n + 1)
    for start, day, need in exams:
        plan[day] = m + 1
    order = sorted(range(m), key=lambda i: exams[i][1])
    for index in order:
        start, day, need = exams[index]
        slot = start
        while slot < day and need > 0:
            if plan[slot] == 0:
                plan[slot] = index + 1
                need -= 1
            slot += 1
        if need > 0:
            return None
    return plan[1:]


# --- clause: main :: () -> None ---
def main():
    n, m, exams = read_input()
    plan = build_schedule(n, m, exams)
    if plan is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()
