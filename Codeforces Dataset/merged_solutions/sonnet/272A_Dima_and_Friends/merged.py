import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    fingers = [int(token) for token in data[1:n + 1]]
    return n, fingers

# Clause safe_choices [Confidence: 0.60]
def safe_choices(n, fingers):
    shown = 0
    for value in fingers:
        shown += value
    people = n + 1
    good = 0
    for mine in range(1, 6):
        if (shown + mine - 1) % people:
            good += 1
    return good

# Clause main [Confidence: 1.00]
def main():
    n, fingers = read_input()
    sys.stdout.write(str(safe_choices(n, fingers)) + "\n")


if __name__ == "__main__":
    main()

