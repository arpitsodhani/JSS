import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]

# Clause has_triangle [Confidence: 0.60]
def has_triangle(n, likes):
    for i in range(1, n + 1):
        b = likes[i - 1]
        c = likes[b - 1]
        if c == i:
            continue
        if likes[c - 1] == i:
            return True
    return False

# Clause main [Confidence: 1.00]
def main():
    n, likes = read_input()
    sys.stdout.write("YES\n" if has_triangle(n, likes) else "NO\n")


if __name__ == "__main__":
    main()

