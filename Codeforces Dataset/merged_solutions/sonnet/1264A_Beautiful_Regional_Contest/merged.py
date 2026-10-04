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
        scores = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, scores))
    return cases

# Clause block_sizes [Confidence: 1.00]
def block_sizes(n, scores):
    sizes = []
    run = 1
    for i in range(1, n):
        if scores[i] == scores[i - 1]:
            run += 1
        else:
            sizes.append(run)
            run = 1
    sizes.append(run)
    return sizes

# Clause award_medals [Confidence: 1.00]
def award_medals(n, sizes):
    limit = n // 2
    gold = sizes[0]
    index = 1
    silver = 0
    while index < len(sizes) and silver <= gold:
        silver += sizes[index]
        index += 1
    if silver <= gold:
        return 0, 0, 0
    bronze = 0
    while index < len(sizes) and gold + silver + bronze + sizes[index] <= limit:
        bronze += sizes[index]
        index += 1
    if bronze <= gold or gold + silver + bronze > limit:
        return 0, 0, 0
    return gold, silver, bronze

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, scores in read_input():
        gold, silver, bronze = award_medals(n, block_sizes(n, scores))
        out.append("%d %d %d" % (gold, silver, bronze))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

