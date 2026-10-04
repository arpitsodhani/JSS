import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()

# Clause fewest_moves [Confidence: 0.80]
def fewest_moves(a, b):
    ups = 0
    downs = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        if a[i] == "4":
            ups += 1
        else:
            downs += 1
    return ups if ups > downs else downs

# Clause main [Confidence: 1.00]
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % fewest_moves(a, b))


if __name__ == "__main__":
    main()

