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

# Clause fewest_inversions [Confidence: 0.80]
def fewest_inversions(a):
    order = sorted(set(a))
    rank = {}
    for i in range(len(order)):
        rank[order[i]] = i + 1
    length_of = len(order) + 1
    tree = [0] * (length_of + 1)
    total = 0
    placed = 0
    for value in a:
        at = rank[value]
        smaller = 0
        i = at - 1
        while i > 0:
            smaller += tree[i]
            i -= i & (-i)
        same = 0
        i = at
        while i > 0:
            same += tree[i]
            i -= i & (-i)
        bigger = placed - same
        total += smaller if smaller < bigger else bigger
        i = at
        while i <= length_of:
            tree[i] += 1
            i += i & (-i)
        placed += 1
    return total

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(fewest_inversions(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

