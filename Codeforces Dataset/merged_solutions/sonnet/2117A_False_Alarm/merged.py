import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((x, data[pos:pos + n]))
        pos += n
    return cases

# Clause can_pass [Confidence: 1.00]
def can_pass(x, doors):
    shut = []
    for i in range(len(doors)):
        if doors[i] == 1:
            shut.append(i)
    if not shut:
        return True
    return shut[-1] - shut[0] + 1 <= x

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for x, doors in read_input():
        lines.append("YES" if can_pass(x, doors) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

