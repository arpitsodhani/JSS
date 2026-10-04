import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]

# Clause gcd_of [Confidence: 1.00]
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a

# Clause best_screen [Confidence: 1.00]
def best_screen(a, b, x, y):
    advance = gcd_of(x, y)
    x //= advance
    y //= advance
    times = a // x
    if b // y < times:
        times = b // y
    if times == 0:
        return 0, 0
    return times * x, times * y

# Clause main [Confidence: 1.00]
def main():
    a, b, x, y = read_input()
    sys.stdout.write("%d %d\n" % best_screen(a, b, x, y))


if __name__ == "__main__":
    main()

