import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    raw = sys.stdin.buffer.read().split()
    x = int(raw[0])
    y = int(raw[1])
    return x, y

# Clause compute_answer [Confidence: 1.00]
def compute_answer(n, m):
    capacity = (n + m) // 3
    return min(n, min(m, capacity))

# Clause main [Confidence: 1.00]
def main():
    n, m = read_input()
    print(compute_answer(n, m))


if __name__ == "__main__":
    main()

