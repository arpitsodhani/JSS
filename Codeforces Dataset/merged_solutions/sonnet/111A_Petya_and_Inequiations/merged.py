import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    n, x, y = map(int, sys.stdin.buffer.read().split()[:3])
    return n, x, y

# Clause solve [Confidence: 0.80]
def solve(n, x, y):
    head = y - (n - 1)
    if head < 1:
        return None
    if head * head + (n - 1) < x:
        return None
    values = [1] * n
    values[0] = head
    return values

# Clause main [Confidence: 1.00]
def main():
    n, x, y = read_input()
    values = solve(n, x, y)
    if values is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join(map(str, values)) + "\n")


if __name__ == "__main__":
    main()

