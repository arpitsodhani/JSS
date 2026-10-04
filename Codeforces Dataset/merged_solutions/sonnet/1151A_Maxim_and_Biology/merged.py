import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1]
    return n, s

# Clause letter_cost [Confidence: 0.40]
def letter_cost(have, want):
    gap = have - want
    if gap < 0:
        gap = -gap
    if gap > 26 - gap:
        return 26 - gap
    return gap

# Clause fewest_changes [Confidence: 1.00]
def fewest_changes(n, s):
    genome = b"ACTG"
    best = -1
    for start in range(n - 3):
        cost = 0
        for offset in range(4):
            cost += letter_cost(s[start + offset], genome[offset])
        if best < 0 or cost < best:
            best = cost
    return best

# Clause main [Confidence: 1.00]
def main():
    n, s = read_input()
    sys.stdout.write(str(fewest_changes(n, s)) + "\n")


if __name__ == "__main__":
    main()

