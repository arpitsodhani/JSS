import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause settle [Confidence: 0.80]
def settle(a):
    collected = []
    for entry in a:
        collected.append(entry - 1 if entry % 2 == 0 else entry)
    return collected

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(" ".join(map(str, settle(read_input()))) + "\n")


if __name__ == "__main__":
    main()

