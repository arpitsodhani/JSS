import sys
LIMIT = 200001

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return cases

# Clause build_prefix [Confidence: 0.80]
def build_prefix():
    prefix = [0] * LIMIT
    power = 3
    depth = 1
    for value in range(1, LIMIT):
        if value >= power:
            power *= 3
            depth += 1
        prefix[value] = prefix[value - 1] + depth
    return prefix

# Clause solve_case [Confidence: 1.00]
def solve_case(l, r, prefix):
    single = prefix[l] - prefix[l - 1]
    return prefix[r] - prefix[l - 1] + single

# Clause main [Confidence: 1.00]
def main():
    prefix = build_prefix()
    out = []
    for l, r in read_input():
        out.append(str(solve_case(l, r, prefix)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

