import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause paint_stones [Confidence: 0.80]
def paint_stones(n, strengths):
    half = n // 2
    zeros = [i for i in range(n) if strengths[i] % 3 == 0]
    nonzeros = [i for i in range(n) if strengths[i] % 3 != 0]
    colour = ["1"] * n
    if len(zeros) <= half:
        coefficient = 0
        picked = list(zeros)
        picked.extend(nonzeros[:half - len(zeros)])
    else:
        coefficient = 2
        picked = list(nonzeros)
        picked.extend(zeros[:half - len(nonzeros)])
    for index in picked:
        colour[index] = "0"
    return coefficient, "".join(colour)

# Clause main [Confidence: 1.00]
def main():
    n, strengths = read_input()
    coefficient, colour = paint_stones(n, strengths)
    sys.stdout.write(str(coefficient) + "\n" + colour + "\n")


if __name__ == "__main__":
    main()

