import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        x = int(data[pos + 1])
        y = int(data[pos + 2])
        pos += 3
        a = data[pos]
        b = data[pos + 1]
        pos += 2
        cases.append((n, x, y, a, b))
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(n, x, y, a, b):
    spots = []
    for i in range(n):
        if a[i] != b[i]:
            spots.append(i)
    count = len(spots)
    if count % 2 == 1:
        return -1
    if count == 0:
        return 0
    if count == 2 and spots[1] - spots[0] == 1:
        if x < 2 * y:
            return x
        return 2 * y
    return (count // 2) * y

# Clause main [Confidence: 1.00]
def main():
    answers = []
    for n, x, y, a, b in read_input():
        answers.append(str(solve_case(n, x, y, a, b)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()

