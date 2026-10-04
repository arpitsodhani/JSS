import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    b = data[1]
    d = data[2]
    return b, d, data[3:3 + n]

# Clause count_empties [Confidence: 0.80]
def count_empties(b, d, sizes):
    waste = 0
    times = 0
    for element in sizes:
        if element > b:
            continue
        waste += element
        if waste > d:
            waste = 0
            times += 1
    return times

# Clause main [Confidence: 1.00]
def main():
    b, d, sizes = read_input()
    sys.stdout.write("%d\n" % count_empties(b, d, sizes))


if __name__ == "__main__":
    main()

