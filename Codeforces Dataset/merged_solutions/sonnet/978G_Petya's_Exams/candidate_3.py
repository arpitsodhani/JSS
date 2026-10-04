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
    for entry in exams:
        plan[entry[1]] = m + 1
    for index in sorted(range(m), key=lambda i: exams[i][1]):
        start, day, need = exams[index]
        free = []
        for slot in range(start, day):
            if plan[slot] == 0:
                free.append(slot)
                if len(free) == need:
                    break
        if len(free) < need:
            return None
        for slot in free:
            plan[slot] = index + 1
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
