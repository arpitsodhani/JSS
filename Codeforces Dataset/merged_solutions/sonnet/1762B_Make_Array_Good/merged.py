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

# Clause raise_to_powers [Confidence: 0.80]
def raise_to_powers(a):
    moves = []
    for index, value in enumerate(a, start=1):
        target = 1
        while target < value:
            target *= 2
        moves.append((index, target - value))
    return moves

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        moves = raise_to_powers(a)
        out.append(str(len(moves)))
        for index, add in moves:
            out.append(str(index) + " " + str(add))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

