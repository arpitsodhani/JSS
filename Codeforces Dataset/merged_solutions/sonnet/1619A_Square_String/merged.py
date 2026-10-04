import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i] for i in range(t)]

# Clause is_square [Confidence: 1.00]
def is_square(s):
    size = len(s)
    if size % 2:
        return "NO"
    half = size // 2
    if s[:half] == s[half:]:
        return "YES"
    return "NO"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for s in read_input():
        out.append(is_square(s))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

