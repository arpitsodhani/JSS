import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause grow [Confidence: 1.00]
def grow(n, k):
    if n % 2:
        d = 3
        smallest = n
        while d * d <= n:
            if n % d == 0:
                smallest = d
                break
            d += 2
        n += smallest
        k -= 1
    return n + 2 * k

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n, k in read_input():
        collected.append(grow(n, k))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

