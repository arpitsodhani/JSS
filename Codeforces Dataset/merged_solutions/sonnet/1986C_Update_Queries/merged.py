import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        m = int(data[pos + 1])
        s = data[pos + 2].decode()
        pos += 3
        ind = [int(data[pos + i]) for i in range(m)]
        pos += m
        c = data[pos].decode()
        pos += 1
        cases.append((s, ind, c))
    return cases

# Clause smallest_string [Confidence: 1.00]
def smallest_string(s, ind, c):
    spots = sorted(set(ind))
    letters = sorted(c)
    out = list(s)
    for i in range(len(spots)):
        out[spots[i] - 1] = letters[i]
    return "".join(out)

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s, ind, c in read_input():
        lines.append(smallest_string(s, ind, c))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

