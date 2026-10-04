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

# Clause smallest_array [Confidence: 1.00]
def smallest_array(a):
    n = len(a)
    suffix = [0] * (n + 1)
    suffix[n] = 10 ** 18
    for i in range(n - 1, -1, -1):
        suffix[i] = a[i] if a[i] < suffix[i + 1] else suffix[i + 1]
    kept = []
    moved = []
    for i in range(n):
        if a[i] > suffix[i + 1]:
            moved.append(a[i] + 1)
        else:
            kept.append(a[i])
    if not moved:
        return kept
    moved.sort()
    bound = moved[0]
    front = []
    for i in range(len(kept)):
        if kept[i] > bound:
            moved.append(kept[i] + 1)
        else:
            front.append(kept[i])
    moved.sort()
    return front + moved

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(" ".join(map(str, smallest_array(a))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

