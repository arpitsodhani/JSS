import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause alice_wins [Confidence: 0.80]
def alice_wins(s):
    ones = 0
    for ch in s:
        if ch == "1":
            ones += 1
    zeros = len(s) - ones
    moves = ones if ones < zeros else zeros
    return moves % 2 == 1

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        collected.append("DA" if alice_wins(s) else "NET")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

