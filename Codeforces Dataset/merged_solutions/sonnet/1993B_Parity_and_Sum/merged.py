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

# Clause fewest_moves [Confidence: 0.80]
def fewest_moves(a):
    evens = sorted(value for value in a if value % 2 == 0)
    odds = [value for value in a if value % 2]
    if not evens or not odds:
        return 0
    largest = max(odds)
    moves = 0
    for value in evens:
        if value > largest:
            return len(evens) + 1
        moves += 1
        largest += value
    return moves

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(fewest_moves(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

