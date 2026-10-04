import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        a = data[pos:pos + n]
        pos += n
        w = data[pos:pos + k]
        pos += k
        cases.append((a, w))
    return cases

# Clause best_happiness [Confidence: 1.00]
def best_happiness(a, w):
    values = sorted(a, reverse=True)
    sizes = sorted(w)
    k = len(sizes)
    amount = 0
    for i in range(k):
        amount += values[i]
        if sizes[i] == 1:
            amount += values[i]
    tail = len(values) - 1
    for i in range(k - 1, -1, -1):
        if sizes[i] == 1:
            continue
        take = sizes[i] - 1
        amount += values[tail]
        tail -= take
    return amount

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, w in read_input():
        out.append(best_happiness(a, w))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

