import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])

# Clause press_counts [Confidence: 0.80]
def press_counts(n):
    out = []
    screen = 2
    for level in range(1, n + 1):
        target = level * (level + 1)
        square = target ** 2
        out.append(str((square - screen) // level))
        screen = target
    return out

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("\n".join(press_counts(read_input())) + "\n")


if __name__ == "__main__":
    main()

