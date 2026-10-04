import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        stacks = []
        for _ in range(3):
            stacks.append(data[pos:pos + n])
            pos += n
        cases.append((x, stacks))
    return cases

# Clause usable_prefix [Confidence: 1.00]
def usable_prefix(x, books):
    gained = 0
    for element in books:
        if element | x != x:
            break
        gained |= element
    return gained

# Clause can_reach [Confidence: 1.00]
def can_reach(x, stacks):
    gained = 0
    for books in stacks:
        gained |= usable_prefix(x, books)
    return gained == x

# Clause main [Confidence: 1.00]
def main():
    out = []
    for x, stacks in read_input():
        out.append("Yes" if can_reach(x, stacks) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

