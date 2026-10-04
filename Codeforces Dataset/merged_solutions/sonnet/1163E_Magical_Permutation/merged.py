import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values

# Clause build_basis [Confidence: 1.00]
def build_basis(values, limit):
    reduced = [0] * 20
    picks = []
    for v in values:
        if v >= limit:
            continue
        cur = v
        for bit in range(19, -1, -1):
            if not cur >> bit & 1:
                continue
            if reduced[bit] == 0:
                reduced[bit] = cur
                picks.append(v)
                cur = 0
                break
            cur ^= reduced[bit]
    return picks

# Clause magical [Confidence: 1.00]
def magical(n, values):
    values.sort()
    best = 0
    chosen = []
    for x in range(0, 19):
        picks = build_basis(values, 1 << x)
        if len(picks) == x:
            best = x
            chosen = picks
    out = [str(best)]
    row = []
    for i in range(1 << best):
        gray = i ^ (i >> 1)
        value = 0
        for bit in range(best):
            if gray >> bit & 1:
                value ^= chosen[bit]
        row.append(str(value))
    out.append(" ".join(row))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, values = read_input()
    sys.stdout.write("\n".join(magical(n, values)) + "\n")


if __name__ == "__main__":
    main()

