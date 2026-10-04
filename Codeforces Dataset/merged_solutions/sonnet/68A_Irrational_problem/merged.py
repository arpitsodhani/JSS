import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[:4], data[4], data[5]

# Clause count_fixed [Confidence: 0.40]
def count_fixed(mods, a, b):
    bound = min(mods)
    high = b if b < bound - 1 else bound - 1
    if high < a:
        return 0
    return high - a + 1

# Clause main [Confidence: 1.00]
def main():
    mods, a, b = read_input()
    sys.stdout.write(str(count_fixed(mods, a, b)) + "\n")


if __name__ == "__main__":
    main()

