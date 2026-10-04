import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_code [Confidence: 0.40]
def build_code(n):
    if n % 2 == 0:
        return None
    return [((2 * i) % n) + 1 for i in range(0, n)]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        code = build_code(n)
        if code is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, code)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

