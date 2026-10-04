import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = [int(token) for token in data[1:n + 1]]
    return n, spots

# Clause postage [Confidence: 1.00]
def postage(n, spots):
    out = []
    for i in range(n):
        if i == 0:
            near = spots[1] - spots[0]
        elif i == n - 1:
            near = spots[n - 1] - spots[n - 2]
        else:
            near = min(spots[i] - spots[i - 1], spots[i + 1] - spots[i])
        far = spots[n - 1] - spots[i]
        other = spots[i] - spots[0]
        if other > far:
            far = other
        out.append("%d %d" % (near, far))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, spots = read_input()
    sys.stdout.write("\n".join(postage(n, spots)) + "\n")


if __name__ == "__main__":
    main()

