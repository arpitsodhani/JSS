import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause exact_root [Confidence: 1.00]
def exact_root(value):
    guess = int(value ** 0.5)
    while guess * guess > value:
        guess -= 1
    while (guess + 1) * (guess + 1) <= value:
        guess += 1
    return guess

# Clause smallest_root [Confidence: 1.00]
def smallest_root(n):
    best = -1
    for s in range(1, 200):
        root = exact_root(s * s + 4 * n)
        if root * root != s * s + 4 * n:
            continue
        if (root - s) % 2:
            continue
        x = (root - s) // 2
        if x <= 0:
            continue
        digits = 0
        value = x
        while value:
            digits += value % 10
            value //= 10
        if digits == s and (best < 0 or x < best):
            best = x
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % smallest_root(read_input()))


if __name__ == "__main__":
    main()

