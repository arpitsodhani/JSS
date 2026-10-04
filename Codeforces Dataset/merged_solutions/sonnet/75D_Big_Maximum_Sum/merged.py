import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    pos = 2
    blocks = []
    for _ in range(n):
        size = data[pos]
        pos += 1
        blocks.append(data[pos:pos + size])
        pos += size
    return blocks, data[pos:pos + m]

# Clause block_stats [Confidence: 1.00]
def block_stats(blocks):
    rows = []
    for values in blocks:
        total = 0
        best = -(1 << 62)
        running = -(1 << 62)
        head = -(1 << 62)
        prefix = 0
        for value in values:
            total += value
            if prefix + value > head:
                head = prefix + value
            prefix += value
            running = value if running < 0 else running + value
            if running > best:
                best = running
        tail = -(1 << 62)
        suffix = 0
        for i in range(len(values) - 1, -1, -1):
            suffix += values[i]
            if suffix > tail:
                tail = suffix
        rows.append((total, head, tail, best))
    return rows

# Clause biggest_sum [Confidence: 1.00]
def biggest_sum(rows, order):
    best = -(1 << 62)
    running = -(1 << 62)
    for index in order:
        total, head, tail, inside = rows[index - 1]
        if inside > best:
            best = inside
        if running > 0:
            joined = running + head
            if joined > best:
                best = joined
            running = running + total
            if tail > running:
                running = tail
        else:
            running = tail
        if running > best:
            best = running
    return best

# Clause main [Confidence: 1.00]
def main():
    blocks, order = read_input()
    sys.stdout.write("%d\n" % biggest_sum(block_stats(blocks), order))


if __name__ == "__main__":
    main()

