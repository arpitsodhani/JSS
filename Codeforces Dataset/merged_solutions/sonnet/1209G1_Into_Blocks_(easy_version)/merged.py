import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return data[2:2 + n]

# Clause value_spans [Confidence: 1.00]
def value_spans(a):
    first = {}
    last = {}
    for i in range(len(a)):
        if a[i] not in first:
            first[a[i]] = i
        last[a[i]] = i
    return first, last

# Clause difficulty [Confidence: 0.80]
def difficulty(a, first, last):
    n = len(a)
    total = 0
    begin = 0
    reach = 0
    counts = {}
    for i in range(n):
        number = a[i]
        counts[number] = counts.get(number, 0) + 1
        if last[number] > reach:
            reach = last[number]
        if i == reach:
            keep = 0
            for other in counts:
                if counts[other] > keep:
                    keep = counts[other]
            total += (i - begin + 1) - keep
            counts = {}
            begin = i + 1
    return total

# Clause main [Confidence: 1.00]
def main():
    a = read_input()
    first, last = value_spans(a)
    sys.stdout.write("%d\n" % difficulty(a, first, last))


if __name__ == "__main__":
    main()

