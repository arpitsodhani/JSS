import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause can_reach [Confidence: 1.00]
def can_reach(x, y):
    if y <= x:
        return True
    if x == 1:
        return False
    if x >= 4:
        return True
    return y <= 3

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for x, y in read_input():
        collected.append("YES" if can_reach(x, y) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

