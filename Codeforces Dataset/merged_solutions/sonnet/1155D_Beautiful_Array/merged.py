import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    return x, data[2:2 + n]

# Clause best_beauty [Confidence: 0.80]
def best_beauty(x, a):
    before = 0
    inside = 0
    after = 0
    best = 0
    for item in a:
        plain = before + item
        if plain < 0:
            plain = 0
        base = before if before > inside else inside
        scaled = base + item * x
        if scaled < 0:
            scaled = 0
        tail = (after if after > inside else inside) + item
        if tail < 0:
            tail = 0
        before = plain
        inside = scaled
        after = tail
        here = before
        if inside > here:
            here = inside
        if after > here:
            here = after
        if here > best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(x, a))


if __name__ == "__main__":
    main()

