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

# Clause square_count [Confidence: 1.00]
def square_count(values, shift):
    total = 0
    for value in values:
        target = shift + value
        root = int(target ** 0.5)
        while root * root > target:
            root -= 1
        while (root + 1) * (root + 1) <= target:
            root += 1
        if root * root == target:
            total += 1
    return total

# Clause best_squareness [Confidence: 1.00]
def best_squareness(values):
    n = len(values)
    best = 1
    for i in range(n):
        for j in range(i + 1, n):
            gap = values[j] - values[i]
            divisor = 1
            while divisor * divisor <= gap:
                if gap % divisor == 0:
                    other = gap // divisor
                    if (divisor + other) % 2 == 0:
                        low = (other - divisor) // 2
                        shift = low * low - values[i]
                        if shift >= 0:
                            here = square_count(values, shift)
                            if here > best:
                                best = here
                divisor += 1
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for case in read_input():
        out.append(str(best_squareness(case)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

