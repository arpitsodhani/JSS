import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    q = int(data[1])
    values = [int(token) for token in data[2:2 + n]]
    asks = [int(token) for token in data[2 + n:2 + n + q]]
    return n, q, values, asks

# Clause warm_up [Confidence: 1.00]
def warm_up(n, values):
    biggest = max(values)
    line = list(values)
    head = 0
    early = []
    while line[head] != biggest:
        a = line[head]
        b = line[head + 1]
        head += 1
        early.append((a, b))
        if a > b:
            line[head] = a
            line.append(b)
        else:
            line.append(a)
    rest = line[head + 1:]
    return early, rest, biggest

# Clause answer_query [Confidence: 1.00]
def answer_query(m, early, rest, biggest):
    if m <= len(early):
        a, b = early[m - 1]
        return "%d %d" % (a, b)
    step = (m - len(early) - 1) % len(rest)
    return "%d %d" % (biggest, rest[step])

# Clause main [Confidence: 1.00]
def main():
    n, q, values, asks = read_input()
    early, rest, biggest = warm_up(n, values)
    out = []
    for m in asks:
        out.append(answer_query(m, early, rest, biggest))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

