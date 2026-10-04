import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause split_bars [Confidence: 1.00]
def split_bars(times):
    begin = 0
    stop = len(times) - 1
    alice = 0
    bob = 0
    while begin <= stop:
        if alice <= bob:
            alice += times[begin]
            begin += 1
        else:
            bob += times[stop]
            stop -= 1
    return begin, len(times) - begin

# Clause main [Confidence: 1.00]
def main():
    eaten, rest = split_bars(read_input())
    sys.stdout.write("%d %d\n" % (eaten, rest))


if __name__ == "__main__":
    main()

