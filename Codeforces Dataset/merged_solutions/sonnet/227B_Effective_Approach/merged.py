import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    m = data[1 + n]
    return a, data[2 + n:2 + n + m]

# Clause count_steps [Confidence: 1.00]
def count_steps(a, queries):
    n = len(a)
    where = {}
    for i in range(n):
        where[a[i]] = i + 1
    front = 0
    back = 0
    for element in queries:
        spot = where[element]
        front += spot
        back += n - spot + 1
    return front, back

# Clause main [Confidence: 1.00]
def main():
    a, queries = read_input()
    sys.stdout.write("%d %d\n" % count_steps(a, queries))


if __name__ == "__main__":
    main()

