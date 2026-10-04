import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    lines = sys.stdin.buffer.read().split()
    first = lines[0].decode()
    second = lines[1].decode()
    return first, second

# Clause compute_answer [Confidence: 0.80]
def compute_answer(x, y):
    result = []
    for xc, yc in zip(x, y):
        if yc > xc:
            return "-1"
        result.append(yc)
    return "".join(result)

# Clause main [Confidence: 1.00]
def main():
    first, second = read_input()
    print(compute_answer(first, second))


if __name__ == "__main__":
    main()

