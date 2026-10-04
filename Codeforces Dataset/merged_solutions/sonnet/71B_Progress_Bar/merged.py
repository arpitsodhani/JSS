import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause bar_state [Confidence: 1.00]
def bar_state(n, k, t):
    amount = t * n * k // 100
    full = amount // k
    squares = []
    for i in range(n):
        if i < full:
            squares.append(k)
        elif i == full:
            squares.append(amount - full * k)
        else:
            squares.append(0)
    return squares

# Clause main [Confidence: 1.00]
def main():
    n, k, t = read_input()
    sys.stdout.write(" ".join(map(str, bar_state(n, k, t))) + "\n")


if __name__ == "__main__":
    main()

