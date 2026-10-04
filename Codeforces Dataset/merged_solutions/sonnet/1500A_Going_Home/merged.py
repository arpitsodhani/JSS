import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause find_quadruple [Confidence: 1.00]
def find_quadruple(n, a):
    seen = {}
    for j in range(n):
        for i in range(j):
            total = a[i] + a[j]
            other = seen.get(total)
            if other is None:
                seen[total] = (i, j)
            else:
                x, y = other
                if x != i and x != j and y != i and y != j:
                    return x + 1, y + 1, i + 1, j + 1
    return None

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    found = find_quadruple(n, a)
    if found is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%d %d %d %d\n" % found)


if __name__ == "__main__":
    main()

