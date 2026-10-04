import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause lifting_moves [Confidence: 0.80]
def lifting_moves(a):
    running = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            running += a[i - 1] - a[i]
    return running

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % lifting_moves(read_input()))


if __name__ == "__main__":
    main()

