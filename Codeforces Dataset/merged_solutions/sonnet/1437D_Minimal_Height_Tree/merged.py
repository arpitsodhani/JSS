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

# Clause min_height [Confidence: 1.00]
def min_height(order):
    n = len(order)
    height = 0
    parents = 1
    index = 1
    while index < n:
        next_parents = 0
        used = 0
        while index < n and used < parents:
            index += 1
            next_parents += 1
            while index < n and order[index] > order[index - 1]:
                index += 1
                next_parents += 1
            used += 1
        parents = next_parents
        height += 1
    return height

# Clause main [Confidence: 1.00]
def main():
    out = []
    for order in read_input():
        out.append(str(min_height(order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

