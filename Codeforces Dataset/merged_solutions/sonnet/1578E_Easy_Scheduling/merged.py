import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        h = int(data[pos])
        p = int(data[pos + 1])
        pos += 2
        cases.append((h, p))
    return cases

# Clause solve_case [Confidence: 1.00]
def solve_case(h, p):
    level = 0
    while level < h and (1 << level) <= p:
        level += 1
    left = (1 << h) - (1 << level)
    return level + (left + p - 1) // p

# Clause main [Confidence: 1.00]
def main():
    answers = []
    for h, p in read_input():
        answers.append(str(solve_case(h, p)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()

