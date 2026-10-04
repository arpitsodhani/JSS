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

# Clause has_balanced [Confidence: 0.80]
def has_balanced(a):
    seen = {0}
    running = 0
    for index in range(len(a)):
        if index & 1:
            running -= a[index]
        else:
            running += a[index]
        if running in seen:
            return True
        seen.add(running)
    return False

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append("YES" if has_balanced(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

