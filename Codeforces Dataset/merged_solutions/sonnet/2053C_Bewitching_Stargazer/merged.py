import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause watched_count [Confidence: 1.00]
def watched_count(length, k):
    known = 0
    weight = 1
    while length >= k:
        if length % 2:
            known += weight
            length = (length - 1) // 2
        else:
            length //= 2
        weight *= 2
    return known

# Clause lucky_value [Confidence: 1.00]
def lucky_value(n, k):
    return watched_count(n, k) * (n + 1) // 2

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for n, k in read_input():
        lines.append(lucky_value(n, k))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

