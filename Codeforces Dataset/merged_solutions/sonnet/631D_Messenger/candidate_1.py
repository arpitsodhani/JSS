import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, str]], list[tuple[int, str]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    long_blocks = []
    for i in range(n):
        piece = data[2 + i].decode()
        size, letter = piece.split("-")
        long_blocks.append((int(size), letter))
    short_blocks = []
    for i in range(m):
        piece = data[2 + n + i].decode()
        size, letter = piece.split("-")
        short_blocks.append((int(size), letter))
    return long_blocks, short_blocks


# --- clause: squeeze :: (blocks: list[tuple[int, str]]) -> list[tuple[int, str]] ---
def squeeze(blocks):
    out = []
    for size, letter in blocks:
        if out and out[-1][1] == letter:
            out[-1] = (out[-1][0] + size, letter)
        else:
            out.append((size, letter))
    return out


# --- clause: count_matches :: (long_blocks: list[tuple[int, str]], short_blocks: list[tuple[int, str]]) -> int ---
def count_matches(long_blocks, short_blocks):
    if len(short_blocks) == 1:
        size, letter = short_blocks[0]
        total = 0
        for length, ch in long_blocks:
            if ch == letter and length >= size:
                total += length - size + 1
        return total
    if len(short_blocks) == 2:
        head = short_blocks[0]
        tail = short_blocks[1]
        total = 0
        for i in range(len(long_blocks) - 1):
            a = long_blocks[i]
            b = long_blocks[i + 1]
            if a[1] == head[1] and b[1] == tail[1] and a[0] >= head[0] and b[0] >= tail[0]:
                total += 1
        return total
    middle = short_blocks[1:-1]
    size = len(middle)
    joined = middle + [(-1, "#")] + long_blocks
    fail = [0] * len(joined)
    for i in range(1, len(joined)):
        step = fail[i - 1]
        while step and joined[i] != joined[step]:
            step = fail[step - 1]
        if joined[i] == joined[step]:
            step += 1
        fail[i] = step
    head = short_blocks[0]
    tail = short_blocks[-1]
    total = 0
    for i in range(len(joined)):
        if fail[i] != size:
            continue
        spot = i - size + 1 - (size + 1)
        left = spot - 1
        right = spot + size
        if left < 0 or right >= len(long_blocks):
            continue
        a = long_blocks[left]
        b = long_blocks[right]
        if a[1] == head[1] and a[0] >= head[0] and b[1] == tail[1] and b[0] >= tail[0]:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    long_blocks, short_blocks = read_input()
    long_blocks = squeeze(long_blocks)
    short_blocks = squeeze(short_blocks)
    sys.stdout.write("%d\n" % count_matches(long_blocks, short_blocks))


if __name__ == "__main__":
    main()
