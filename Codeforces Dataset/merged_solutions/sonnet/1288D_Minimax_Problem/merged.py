import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    rows = []
    pos = 2
    for _ in range(n):
        rows.append(data[pos:pos + m])
        pos += m
    return n, m, rows

# Clause pair_for [Confidence: 1.00]
def pair_for(n, m, rows, limit):
    full = (1 << m) - 1
    owner = {}
    for index in range(n):
        mask = 0
        row = rows[index]
        for bit in range(m):
            if row[bit] >= limit:
                mask |= 1 << bit
        if mask not in owner:
            owner[mask] = index + 1
    for first in owner:
        for second in owner:
            if first | second == full:
                return owner[first], owner[second]
    return None

# Clause best_pair [Confidence: 1.00]
def best_pair(n, m, rows):
    values = sorted({value for row in rows for value in row})
    low = 0
    high = len(values) - 1
    answer = pair_for(n, m, rows, values[0])
    while low <= high:
        middle = (low + high) // 2
        found = pair_for(n, m, rows, values[middle])
        if found is not None:
            answer = found
            low = middle + 1
        else:
            high = middle - 1
    return answer

# Clause main [Confidence: 1.00]
def main():
    n, m, rows = read_input()
    first, second = best_pair(n, m, rows)
    sys.stdout.write("%d %d\n" % (first, second))


if __name__ == "__main__":
    main()

