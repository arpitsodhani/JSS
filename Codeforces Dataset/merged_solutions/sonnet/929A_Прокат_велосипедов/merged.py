import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause fewest_bikes [Confidence: 1.00]
def fewest_bikes(k, x):
    n = len(x)
    at = 0
    taken = 0
    while at < n - 1:
        reach = x[at] + k
        advance = at
        for j in range(at + 1, n):
            if x[j] <= reach:
                advance = j
            else:
                break
        if advance == at:
            return -1
        at = advance
        taken += 1
    return taken

# Clause main [Confidence: 1.00]
def main():
    k, x = read_input()
    sys.stdout.write("%d\n" % fewest_bikes(k, x))


if __name__ == "__main__":
    main()

