import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause evaluate [Confidence: 0.80]
def evaluate(text):
    left = int(text[0])
    right = int(text[2])
    return left + right

# Clause main [Confidence: 1.00]
def main():
    out = []
    for item in read_input():
        out.append(str(evaluate(item)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

