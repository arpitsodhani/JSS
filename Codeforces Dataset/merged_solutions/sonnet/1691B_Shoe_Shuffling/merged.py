import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause shuffle_shoes [Confidence: 1.00]
def shuffle_shoes(sizes):
    n = len(sizes)
    order = list(range(1, n + 1))
    start = 0
    while start < n:
        closing = start
        while closing + 1 < n and sizes[closing + 1] == sizes[start]:
            closing += 1
        if closing == start:
            return None
        for i in range(start, closing + 1):
            order[i] = start + 1 + (i - start + 1) % (closing - start + 1)
        start = closing + 1
    return order

# Clause main [Confidence: 1.00]
def main():
    out = []
    for sizes in read_input():
        order = shuffle_shoes(sizes)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

