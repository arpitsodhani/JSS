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

# Clause prime_counts [Confidence: 1.00]
def prime_counts(a):
    tally = {}
    for entry in a:
        rest = entry
        d = 2
        while d * d <= rest:
            while rest % d == 0:
                tally[d] = tally.get(d, 0) + 1
                rest //= d
            d += 1
        if rest > 1:
            tally[rest] = tally.get(rest, 0) + 1
    return tally

# Clause most_groups [Confidence: 1.00]
def most_groups(tally):
    groups = 0
    spare = 0
    for prime in tally:
        groups += tally[prime] // 2
        spare += tally[prime] % 2
    return groups + spare // 3

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        out.append(most_groups(prime_counts(a)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

