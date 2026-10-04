import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause build_array [Confidence: 1.00]
def build_array(n):
    collected = []
    for entry in range(n, 0, -1):
        collected.append(entry)
    collected.append(n)
    for entry in range(1, n):
        collected.append(entry)
    return collected

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        collected.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

