import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause best_average [Confidence: 1.00]
def best_average(k, a):
    n = len(a)
    cumulative = [0] * (n + 1)
    for i in range(n):
        cumulative[i + 1] = cumulative[i] + a[i]
    best = 0.0
    for length in range(k, n + 1):
        for start in range(n - length + 1):
            entry = (cumulative[start + length] - cumulative[start]) / float(length)
            if entry > best:
                best = entry
    return best

# Clause main [Confidence: 1.00]
def main():
    k, a = read_input()
    sys.stdout.write("%.15f\n" % best_average(k, a))


if __name__ == "__main__":
    main()

