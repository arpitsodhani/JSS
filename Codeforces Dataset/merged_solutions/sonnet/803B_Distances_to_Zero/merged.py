import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause zero_distances [Confidence: 0.80]
def zero_distances(a):
    n = len(a)
    far = n + 1
    dist = [far] * n
    last = -far
    for i in range(n):
        if a[i] == 0:
            last = i
        dist[i] = i - last
    last = 2 * far
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last = i
        if last - i < dist[i]:
            dist[i] = last - i
    return dist

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(" ".join(map(str, zero_distances(read_input()))) + "\n")


if __name__ == "__main__":
    main()

