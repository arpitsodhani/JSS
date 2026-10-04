import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        a = data[pos:pos + n - 1]
        pos += n - 1
        b = data[pos:pos + n]
        pos += n
        cases.append((m, a, b))
    return cases

# Clause removals_for [Confidence: 1.00]
def removals_for(first, a, b):
    begin = a + [first]
    begin.sort()
    n = len(begin)
    matched = 0
    i = 0
    for value in b:
        if i < n and begin[i] < value:
            matched += 1
            i += 1
    return n - matched

# Clause total_removals [Confidence: 1.00]
def total_removals(m, a, b):
    a = sorted(a)
    b = sorted(b)
    low_cost = removals_for(1, a, b)
    high_cost = removals_for(m, a, b)
    if low_cost == high_cost:
        return m * low_cost
    low = 1
    high = m
    while low < high:
        mid = (low + high) // 2
        if removals_for(mid, a, b) > low_cost:
            high = mid
        else:
            low = mid + 1
    return (low - 1) * low_cost + (m - low + 1) * high_cost

# Clause main [Confidence: 1.00]
def main():
    out = []
    for m, a, b in read_input():
        out.append(total_removals(m, a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

