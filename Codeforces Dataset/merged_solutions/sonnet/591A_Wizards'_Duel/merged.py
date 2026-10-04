import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]

# Clause meeting_point [Confidence: 1.00]
def meeting_point(l, p, q):
    share = p / (p + q)
    return l * share

# Clause main [Confidence: 1.00]
def main():
    l, p, q = read_input()
    sys.stdout.write("%.10f\n" % meeting_point(l, p, q))


if __name__ == "__main__":
    main()

