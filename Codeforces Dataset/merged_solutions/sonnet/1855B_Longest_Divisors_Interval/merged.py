import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause longest_run [Confidence: 0.80]
def longest_run(n):
    advance = 1
    while n % advance == 0:
        advance += 1
    return advance - 1

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n in read_input():
        lines.append(longest_run(n))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

