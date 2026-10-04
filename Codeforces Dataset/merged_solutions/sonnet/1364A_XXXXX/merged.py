import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((x, data[pos:pos + n]))
        pos += n
    return cases

# Clause longest_piece [Confidence: 1.00]
def longest_piece(x, a):
    n = len(a)
    if sum(a) % x:
        return n
    first = -1
    last = -1
    for i in range(n):
        if a[i] % x:
            if first < 0:
                first = i
            last = i
    if first < 0:
        return -1
    tail = n - first - 1
    return tail if tail > last else last

# Clause main [Confidence: 1.00]
def main():
    out = []
    for x, a in read_input():
        out.append(longest_piece(x, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

