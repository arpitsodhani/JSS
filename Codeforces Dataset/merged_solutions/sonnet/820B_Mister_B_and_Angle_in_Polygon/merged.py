import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]

# Clause best_arc [Confidence: 0.80]
def best_arc(n, a):
    target = a * n
    choices = range(1, n - 1)
    best = 1
    gap = None
    for arc in choices:
        here = arc * 180 - target
        if here < 0:
            here = -here
        if gap is None or here < gap:
            gap = here
            best = arc
    return best

# Clause main [Confidence: 1.00]
def main():
    n, a = read_input()
    arc = best_arc(n, a)
    sys.stdout.write("1 2 %d\n" % (n + 1 - arc))


if __name__ == "__main__":
    main()

