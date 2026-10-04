import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(a):
    n = len(a)
    order = list(a)
    rounds = 0
    while order != sorted(order):
        start = rounds % 2
        for i in range(start, n - 1, 2):
            if order[i] > order[i + 1]:
                order[i], order[i + 1] = order[i + 1], order[i]
        rounds += 1
    return rounds

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

