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

# Clause count_inversions [Confidence: 1.00]
def count_inversions(a):
    ones = 0
    total = 0
    for entry in a:
        if entry:
            ones += 1
        else:
            total += ones
    return total

# Clause best_after_flip [Confidence: 1.00]
def best_after_flip(a):
    best = count_inversions(a)
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
            here = count_inversions(a)
            a[i] = 0
            if here > best:
                best = here
            break
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            a[i] = 0
            here = count_inversions(a)
            a[i] = 1
            if here > best:
                best = here
            break
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(best_after_flip(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

