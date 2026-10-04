import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases

# Clause keep_table [Confidence: 1.00]
def keep_table(n, colours):
    values = [0] + colours
    best = [[-1] * (n + 2) for _ in range(n + 2)]
    best[0][0] = 0
    for gaps in range(0, n + 1):
        for i in range(1, n + 1):
            top = -1
            for prev in range(0, i):
                if best[prev][gaps if prev == i - 1 else gaps - 1] < 0:
                    continue
                if values[prev] >= values[i]:
                    continue
                cost = best[prev][gaps if prev == i - 1 else gaps - 1]
                if cost > top:
                    top = cost
            if top >= 0:
                best[i][gaps] = top + 1
    return best

# Clause min_coins [Confidence: 1.00]
def min_coins(n, best):
    out = []
    for k in range(1, n + 1):
        kept = 0
        for i in range(0, n + 1):
            for gaps in range(0, k + 1):
                if best[i][gaps] < 0:
                    continue
                used = gaps + (1 if i < n else 0)
                if used <= k and best[i][gaps] > kept:
                    kept = best[i][gaps]
        out.append(str(n - kept))
    return out

# Clause main [Confidence: 1.00]
def main():
    out = []
    for colours in read_input():
        n = len(colours)
        out.append(" ".join(min_coins(n, keep_table(n, colours))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

