import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()

# Clause fewest_changes [Confidence: 0.80]
def fewest_changes(s, u):
    best = 0
    for begin in range(-len(u), len(s) + 1):
        same = 0
        for i in range(len(u)):
            at = begin + i
            if 0 <= at < len(s) and s[at] == u[i]:
                same += 1
        if same > best:
            best = same
    return len(u) - best

# Clause main [Confidence: 1.00]
def main():
    s, u = read_input()
    sys.stdout.write("%d\n" % fewest_changes(s, u))


if __name__ == "__main__":
    main()

