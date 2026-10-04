import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + 2 * n]

# Clause can_split [Confidence: 0.80]
def can_split(n, ratings):
    arranged = sorted(ratings)
    return arranged[n - 1] < arranged[n]

# Clause main [Confidence: 1.00]
def main():
    n, ratings = read_input()
    sys.stdout.write("YES\n" if can_split(n, ratings) else "NO\n")


if __name__ == "__main__":
    main()

