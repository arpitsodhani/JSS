import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode(), data[3].decode()

# Clause count_prefixes [Confidence: 1.00]
def count_prefixes(k, s, t):
    amount = 0
    width = 1
    for i in range(len(s)):
        if width < k:
            width *= 2
            if s[i] == "b":
                width -= 1
            if t[i] == "a":
                width -= 1
            if width > k:
                width = k
        amount += width
    return amount

# Clause main [Confidence: 1.00]
def main():
    k, s, t = read_input()
    sys.stdout.write("%d\n" % count_prefixes(k, s, t))


if __name__ == "__main__":
    main()

