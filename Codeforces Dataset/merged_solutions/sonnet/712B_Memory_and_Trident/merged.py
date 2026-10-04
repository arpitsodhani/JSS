import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause fewest_edits [Confidence: 0.80]
def fewest_edits(s):
    if len(s) % 2:
        return -1
    across = 0
    up = 0
    for ch in s:
        if ch == "L":
            across -= 1
        elif ch == "R":
            across += 1
        elif ch == "U":
            up += 1
        else:
            up -= 1
    return (abs(across) + abs(up)) // 2

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % fewest_edits(read_input()))


if __name__ == "__main__":
    main()

