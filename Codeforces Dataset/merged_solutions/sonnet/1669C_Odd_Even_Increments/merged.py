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

# Clause can_align [Confidence: 0.80]
def can_align(a):
    for head_pos in range(2):
        first = a[head_pos] % 2
        for i in range(head_pos, len(a), 2):
            if a[i] % 2 != first:
                return False
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_align(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

