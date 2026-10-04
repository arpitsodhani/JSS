import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause minutes_needed [Confidence: 0.40]
def minutes_needed(n):
    if n == 1:
        return 2
    return (n + 2) // 3

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n in read_input():
        out.append(str(minutes_needed(n)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

