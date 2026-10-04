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

# Clause value_spots [Confidence: 1.00]
def value_spots(a):
    n = len(a)
    spots = [[] for _ in range(27)]
    counts = [[0] * (n + 1) for _ in range(27)]
    for i in range(n):
        spots[a[i]].append(i)
        for entry in range(1, 27):
            counts[entry][i + 1] = counts[entry][i]
        counts[a[i]][i + 1] += 1
    return spots, counts

# Clause longest_palindrome [Confidence: 1.00]
def longest_palindrome(a, spots, counts):
    n = len(a)
    best = 0
    for entry in range(1, 27):
        here = spots[entry]
        if len(here) > best:
            best = len(here)
        for x in range(1, len(here) // 2 + 1):
            left = here[x - 1]
            right = here[len(here) - x]
            for other in range(1, 27):
                middle = counts[other][right] - counts[other][left + 1]
                if 2 * x + middle > best:
                    best = 2 * x + middle
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for a in read_input():
        spots, counts = value_spots(a)
        out.append(longest_palindrome(a, spots, counts))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

