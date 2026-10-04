import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause winner [Confidence: 1.00]
def winner(n):
    if n % 2:
        return "Bob"
    power = 0
    element = n
    while element % 2 == 0:
        element //= 2
        power += 1
    if element > 1:
        return "Alice"
    if power % 2:
        return "Bob"
    return "Alice"

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n in read_input():
        lines.append(winner(n))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

