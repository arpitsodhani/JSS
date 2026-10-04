import sys


# --- clause: read_input :: () -> tuple[list[list[int]], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    reader = 2
    blocks = []
    for _ in range(n):
        size = numbers[reader]
        reader += 1
        blocks.append(numbers[reader:reader + size])
        reader += size
    return blocks, numbers[reader:reader + m]


# --- clause: block_stats :: (blocks: list[list[int]]) -> list[tuple[int, int, int, int]] ---
def block_stats(blocks):
    rows = []
    for values in blocks:
        size = len(values)
        prefix = [0] * (size + 1)
        for i in range(size):
            prefix[i + 1] = prefix[i] + values[i]
        total = prefix[size]
        head = max(prefix[i] for i in range(1, size + 1))
        tail = max(total - prefix[i] for i in range(size))
        best = -(1 << 62)
        lowest = 0
        for i in range(1, size + 1):
            if prefix[i] - lowest > best:
                best = prefix[i] - lowest
            if prefix[i] < lowest:
                lowest = prefix[i]
        rows.append((total, head, tail, best))
    return rows


# --- clause: biggest_sum :: (rows: list[tuple[int, int, int, int]], order: list[int]) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    blocks, order = read_input()
    sys.stdout.write("%d\n" % biggest_sum(block_stats(blocks), order))


if __name__ == "__main__":
    main()
