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

# Clause group_order [Confidence: 1.00]
def group_order(a):
    spots = {}
    for i in range(len(a)):
        if a[i] in spots:
            spots[a[i]].append(i)
        else:
            spots[a[i]] = [i]
    ranked = sorted(spots, key=lambda entry: -len(spots[entry]))
    order = []
    for entry in ranked:
        order.extend(spots[entry])
    return order, len(spots[ranked[0]])

# Clause shuffled [Confidence: 1.00]
def shuffled(a, order, shift):
    n = len(a)
    out = [0] * n
    for i in range(n):
        out[order[i]] = a[order[(i + shift) % n]]
    return out

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        order, shift = group_order(a)
        out.append(" ".join(map(str, shuffled(a, order, shift))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

