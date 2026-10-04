import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause find_triple [Confidence: 0.80]
def find_triple(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            for k in range(j + 1, n):
                if k == i:
                    continue
                if a[i] == a[j] + a[k]:
                    return i + 1, j + 1, k + 1
    return None

# Clause main [Confidence: 1.00]
def main():
    discovered = find_triple(read_input())
    if discovered is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%d %d %d\n" % discovered)


if __name__ == "__main__":
    main()

