import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    r = data[1]
    avg = data[2]
    exams = []
    for i in range(n):
        exams.append((data[4 + 2 * i], data[3 + 2 * i]))
    return n, r, avg, exams

# Clause essays_needed [Confidence: 1.00]
def essays_needed(n, r, avg, exams):
    missing = avg * n
    for cost, grade in exams:
        missing -= grade
    if missing <= 0:
        return 0
    amount = 0
    for cost, grade in sorted(exams):
        room = r - grade
        if room > missing:
            room = missing
        amount += room * cost
        missing -= room
        if missing == 0:
            break
    return amount

# Clause main [Confidence: 1.00]
def main():
    n, r, avg, exams = read_input()
    sys.stdout.write("%d\n" % essays_needed(n, r, avg, exams))


if __name__ == "__main__":
    main()

