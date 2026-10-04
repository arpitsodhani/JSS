import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause schedule [Confidence: 1.00]
def schedule(k, a):
    n = len(a)
    free = [0] * k
    spans = []
    for i in range(n):
        best = 0
        for j in range(1, k):
            if free[j] < free[best]:
                best = j
        begin = free[best]
        free[best] = begin + a[i]
        spans.append((begin, free[best]))
    return spans

# Clause count_interesting [Confidence: 0.80]
def count_interesting(spans):
    n = len(spans)
    horizon = max(end for begin, end in spans) + 2
    done = [0] * horizon
    for begin, end in spans:
        done[end] += 1
    for time in range(1, horizon):
        done[time] += done[time - 1]
    total = 0
    for begin, end in spans:
        for time in range(begin, end):
            if (200 * done[time] + n) // (2 * n) == time - begin + 1:
                total += 1
                break
    return total

# Clause main [Confidence: 1.00]
def main():
    k, a = read_input()
    sys.stdout.write("%d\n" % count_interesting(schedule(k, a)))


if __name__ == "__main__":
    main()

