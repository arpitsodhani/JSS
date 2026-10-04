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
        m = int(data[pos + 1])
        pos += 2
        garden = [int(token) for token in data[pos:pos + n]]
        pos += n
        wanted = [int(token) for token in data[pos:pos + m]]
        pos += m
        cases.append((n, m, garden, wanted))
    return cases

# Clause match_counts [Confidence: 1.00]
def match_counts(n, m, garden, wanted):
    left = [0] * (n + 1)
    taken = 0
    for i in range(n):
        if taken < m and garden[i] >= wanted[taken]:
            taken += 1
        left[i + 1] = taken
    right = [0] * (n + 2)
    taken = 0
    for i in range(n - 1, -1, -1):
        if taken < m and garden[i] >= wanted[m - 1 - taken]:
            taken += 1
        right[i] = taken
    return left, right

# Clause smallest_wand [Confidence: 1.00]
def smallest_wand(n, m, wanted, left, right):
    best = -1
    for cut in range(n + 1):
        have = left[cut] + right[cut]
        if have >= m:
            return 0
        if have == m - 1:
            need = wanted[left[cut]]
            if best < 0 or need < best:
                best = need
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, m, garden, wanted in read_input():
        left, right = match_counts(n, m, garden, wanted)
        out.append(str(smallest_wand(n, m, wanted, left, right)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

