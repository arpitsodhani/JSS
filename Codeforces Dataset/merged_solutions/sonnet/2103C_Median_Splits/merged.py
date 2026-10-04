import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases

# Clause running_sums [Confidence: 1.00]
def running_sums(k, a):
    sums = [0]
    for element in a:
        sums.append(sums[-1] + (1 if element <= k else -1))
    return sums

# Clause split_exists [Confidence: 1.00]
def split_exists(sums):
    n = len(sums) - 1
    total = sums[n]
    best_nonneg = None
    seen_nonneg = False
    lowest = None
    for r in range(2, n):
        left = r - 1
        if sums[left] >= 0:
            seen_nonneg = True
            if best_nonneg is None or sums[left] < best_nonneg:
                best_nonneg = sums[left]
        if lowest is None or sums[left] < lowest:
            lowest = sums[left]
        if best_nonneg is not None and best_nonneg <= sums[r]:
            return True
        if seen_nonneg and sums[r] <= total:
            return True
        if sums[r] <= total and lowest is not None and lowest <= sums[r]:
            return True
    return False

# Clause main [Confidence: 1.00]
def main():
    out = []
    for k, a in read_input():
        out.append("YES" if split_exists(running_sums(k, a)) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

