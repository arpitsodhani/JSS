import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    return m, data[2:2 + n]

# Clause pages_written [Confidence: 1.00]
def pages_written(a, days):
    amount = 0
    for i in range(len(a)):
        gain = a[i] - i // days
        if gain <= 0:
            break
        amount += gain
    return amount

# Clause fewest_days [Confidence: 1.00]
def fewest_days(m, a):
    a = sorted(a, reverse=True)
    if sum(a) < m:
        return -1
    bottom = 1
    high = len(a)
    while bottom < high:
        mid = (bottom + high) // 2
        if pages_written(a, mid) >= m:
            high = mid
        else:
            bottom = mid + 1
    return bottom

# Clause main [Confidence: 1.00]
def main():
    m, a = read_input()
    sys.stdout.write("%d\n" % fewest_days(m, a))


if __name__ == "__main__":
    main()

