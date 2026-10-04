import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_string [Confidence: 0.60]
def build_string(n):
    if n == 1:
        return "a"
    if n % 2 == 0:
        left = n // 2
        return "a" * left + "b" + "a" * (left - 1)
    left = n // 2
    return "a" * left + "b" + "a" * (left - 1) + "c"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(build_string(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

