import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:n + 1]))
    return n, values

# Clause best_power [Confidence: 0.80]
def best_power(n, values):
    best = 1
    for value in values:
        power = value & -value
        if power > best:
            best = power
    count = 0
    for value in values:
        if value % best == 0:
            count += 1
    return best, count

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    power, count = best_power(n, values)
    sys.stdout.write("%d %d\n" % (power, count))


if __name__ == "__main__":
    main()

