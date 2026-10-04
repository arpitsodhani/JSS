import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause missed_meals [Confidence: 0.80]
def missed_meals(b, d, s):
    days = b
    if d > days:
        days = d
    if s > days:
        days = s
    running = 0
    for hits in (b, d, s):
        if days - 1 - hits > 0:
            running += days - 1 - hits
    return running

# Clause main [Confidence: 1.00]
def main():
    b, d, s = read_input()
    sys.stdout.write("%d\n" % missed_meals(b, d, s))


if __name__ == "__main__":
    main()

