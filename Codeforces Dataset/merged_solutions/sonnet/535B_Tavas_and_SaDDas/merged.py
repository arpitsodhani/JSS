import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause lucky_index [Confidence: 0.80]
def lucky_index(n):
    extent = len(n)
    shorter = (1 << extent) - 2
    inside = 0
    for ch in n:
        inside = inside * 2 + (1 if ch == "7" else 0)
    return shorter + inside + 1

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % lucky_index(read_input()))


if __name__ == "__main__":
    main()

