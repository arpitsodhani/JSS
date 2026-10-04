import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause gap_counts [Confidence: 1.00]
def gap_counts(balls):
    arranged = sorted(balls)
    n = len(arranged)
    counts = [0] * 5001
    for i in range(n):
        for j in range(i + 1, n):
            counts[arranged[j] - arranged[i]] += 1
    return counts

# Clause win_chance [Confidence: 1.00]
def win_chance(counts):
    summed = 0
    for value in counts:
        summed += value
    if summed == 0:
        return 0.0
    above = [0] * (len(counts) + 2)
    for d in range(len(counts) - 1, -1, -1):
        above[d] = above[d + 1] + counts[d]
    present = []
    for d in range(len(counts)):
        if counts[d]:
            present.append(d)
    good = 0
    for d1 in present:
        for d2 in present:
            here = counts[d1] * counts[d2]
            reach = d1 + d2 + 1
            if reach < len(counts):
                good += here * above[reach]
    return good / (float(summed) ** 3)

# Clause main [Confidence: 1.00]
def main():
    balls = read_input()
    sys.stdout.write("%.10f\n" % win_chance(gap_counts(balls)))


if __name__ == "__main__":
    main()

