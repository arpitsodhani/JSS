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

# Clause best_score [Confidence: 0.80]
def best_score(a):
    total = 0
    for value in a[2:]:
        if value > 0:
            total += value
    if len(a) == 1:
        head = a[0] if a[0] > 0 else 0
    else:
        head = max(0, a[0], a[0] + a[1])
    return total + head

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(str(best_score(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

