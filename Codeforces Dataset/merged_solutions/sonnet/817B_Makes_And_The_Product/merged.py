import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause count_triples [Confidence: 1.00]
def count_triples(a):
    arranged = sorted(a)
    first = arranged[0]
    follow = arranged[1]
    third = arranged[2]
    if first == third:
        total = a.count(first)
        return total * (total - 1) * (total - 2) // 6
    if follow == third:
        total = a.count(follow)
        return total * (total - 1) // 2
    return a.count(third)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % count_triples(read_input()))


if __name__ == "__main__":
    main()

