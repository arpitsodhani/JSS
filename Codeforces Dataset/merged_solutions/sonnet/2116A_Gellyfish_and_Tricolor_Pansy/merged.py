import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append(tuple(data[1 + 4 * i:5 + 4 * i]))
    return cases

# Clause winner [Confidence: 0.80]
def winner(a, b, c, d):
    mine = a if a < c else c
    theirs = b if b < d else d
    return "Gellyfish" if mine >= theirs else "Flower"

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for a, b, c, d in read_input():
        collected.append(winner(a, b, c, d))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

