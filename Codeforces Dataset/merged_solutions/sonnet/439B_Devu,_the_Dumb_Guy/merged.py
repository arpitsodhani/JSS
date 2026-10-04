import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    return x, data[2:2 + n]

# Clause teaching_time [Confidence: 1.00]
def teaching_time(x, chapters):
    amount = 0
    for count in sorted(chapters):
        amount += count * x
        if x > 1:
            x -= 1
    return amount

# Clause main [Confidence: 1.00]
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()

