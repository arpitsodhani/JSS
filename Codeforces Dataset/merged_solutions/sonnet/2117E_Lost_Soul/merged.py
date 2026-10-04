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
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases

# Clause best_prefix [Confidence: 1.00]
def best_prefix(a, b):
    n = len(a)
    seen = [[0, 0] for _ in range(n + 1)]
    for position in range(n, 0, -1):
        value_a = a[position - 1]
        value_b = b[position - 1]
        colour_a = position & 1
        colour_b = (position + 1) & 1
        if value_a == value_b:
            return position
        if seen[value_a][1 - colour_a]:
            return position
        if seen[value_b][1 - colour_b]:
            return position
        far_a = seen[value_a][colour_a]
        far_b = seen[value_b][colour_b]
        if position < n:
            next_a = a[position]
            next_b = b[position]
            next_colour_a = (position + 1) & 1
            next_colour_b = position & 1
            if next_a == value_a and next_colour_a == colour_a:
                far_a -= 1
            if next_b == value_a and next_colour_b == colour_a:
                far_a -= 1
            if next_a == value_b and next_colour_a == colour_b:
                far_b -= 1
            if next_b == value_b and next_colour_b == colour_b:
                far_b -= 1
        if far_a > 0 or far_b > 0:
            return position
        seen[value_a][colour_a] += 1
        seen[value_b][colour_b] += 1
    return 0

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a, b in read_input():
        out.append(str(best_prefix(a, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

