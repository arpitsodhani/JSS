import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause enough_room [Confidence: 1.00]
def enough_room(n, k, d):
    room = 1
    for _ in range(d):
        room *= k
        if room >= n:
            return True
    return room >= n

# Clause seat_plan [Confidence: 1.00]
def seat_plan(n, k, d):
    rows = [[0] * n for _ in range(d)]
    for student in range(n):
        element = student
        for day in range(d):
            rows[day][student] = element % k + 1
            element //= k
    return rows

# Clause main [Confidence: 1.00]
def main():
    n, k, d = read_input()
    if not enough_room(n, k, d):
        sys.stdout.write("-1\n")
        return
    out = []
    for line in seat_plan(n, k, d):
        out.append(" ".join(map(str, line)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

