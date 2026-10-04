import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values

# Clause is_square [Confidence: 0.40]
def is_square(value):
    if value < 0:
        return False
    root = int(value ** 0.5)
    while root * root > value:
        root -= 1
    while (root + 1) * (root + 1) <= value:
        root += 1
    return root * root == value

# Clause largest_plain [Confidence: 0.60]
def largest_plain(n, values):
    best = None
    for value in values:
        if is_square(value):
            continue
        if best is None or value > best:
            best = value
    return best

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    sys.stdout.write(str(largest_plain(n, values)) + "\n")


if __name__ == "__main__":
    main()

