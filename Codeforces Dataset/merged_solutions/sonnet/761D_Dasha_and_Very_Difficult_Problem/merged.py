import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    l = data[1]
    r = data[2]
    return l, r, data[3:3 + n], data[3 + n:3 + 2 * n]

# Clause rebuild_b [Confidence: 1.00]
def rebuild_b(l, r, a, p):
    n = len(a)
    arranged = sorted(range(n), key=lambda i: p[i])
    b = [0] * n
    previous = None
    for i in arranged:
        want = l - a[i]
        if previous is not None and previous + 1 > want:
            want = previous + 1
        if a[i] + want > r:
            return None
        b[i] = a[i] + want
        previous = want
    return b

# Clause main [Confidence: 1.00]
def main():
    l, r, a, p = read_input()
    b = rebuild_b(l, r, a, p)
    if b is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, b)) + "\n")


if __name__ == "__main__":
    main()

