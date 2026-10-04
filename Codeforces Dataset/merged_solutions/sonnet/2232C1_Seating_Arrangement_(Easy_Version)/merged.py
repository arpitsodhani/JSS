import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        s = int(data[pos + 2])
        line = data[pos + 3].decode()
        pos += 4
        cases.append((n, x, s, line))
    return cases

# Clause seat_people [Confidence: 1.00]
def seat_people(n, x, s, line):
    tables = 0
    seated = 0
    lonely = 0
    for person in line:
        free = tables * s - seated
        if person == "I":
            if tables < x:
                tables += 1
                seated += 1
            continue
        if free == 0 and lonely > 0 and tables < x:
            tables += 1
            lonely -= 1
            free = tables * s - seated
        if free > 0:
            seated += 1
            if person == "A":
                lonely += 1
        elif person == "A" and tables < x:
            tables += 1
            seated += 1
    return seated

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, x, s, line in read_input():
        out.append(str(seat_people(n, x, s, line)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

