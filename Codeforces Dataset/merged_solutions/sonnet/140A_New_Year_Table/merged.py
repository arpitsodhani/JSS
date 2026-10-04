import math
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause plates_fit [Confidence: 1.00]
def plates_fit(n, big, small):
    if small > big:
        return False
    if n == 1:
        return True
    if 2 * small > big:
        return False
    return (big - small) * math.sin(math.pi / n) >= small - 1e-9

# Clause main [Confidence: 1.00]
def main():
    n, big, small = read_input()
    sys.stdout.write("YES\n" if plates_fit(n, big, small) else "NO\n")


if __name__ == "__main__":
    main()

