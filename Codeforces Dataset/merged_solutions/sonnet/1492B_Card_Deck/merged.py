import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases

# Clause best_deck [Confidence: 1.00]
def best_deck(p):
    n = len(p)
    top = [0] * n
    where = 0
    for i in range(n):
        if p[i] > p[where]:
            where = i
        top[i] = where
    lines = []
    end = n
    while end > 0:
        start = top[end - 1]
        lines.extend(p[start:end])
        end = start
    return lines

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for p in read_input():
        lines.append(" ".join(map(str, best_deck(p))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

