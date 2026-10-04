import sys

# Clause read_input [Confidence: 1.00]
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

# Clause build_schedule [Confidence: 1.00]
def build_schedule(n, m, exams):
    plan = [0] * (n + 1)
    for start, day, need in exams:
        plan[day] = m + 1
    deadlines = sorted(range(m), key=lambda i: exams[i][1])
    for index in deadlines:
        start, day, need = exams[index]
        remaining = need
        slot = start
        while slot < day:
            if remaining == 0:
                break
            if plan[slot] == 0:
                plan[slot] = index + 1
                remaining -= 1
            slot += 1
        if remaining:
            return None
    return plan[1:]

# Clause main [Confidence: 1.00]
def main():
    n, m, exams = read_input()
    plan = build_schedule(n, m, exams)
    if plan is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, plan)) + "\n")


if __name__ == "__main__":
    main()

