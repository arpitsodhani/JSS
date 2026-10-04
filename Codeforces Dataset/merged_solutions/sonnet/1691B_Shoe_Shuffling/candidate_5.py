import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: shuffle_shoes :: (sizes: list[int]) -> list[int] | None ---
def shuffle_shoes(sizes):
    n = len(sizes)
    order = list(range(1, n + 1))
    start = 0
    while start < n:
        tail_pos = start
        while tail_pos + 1 < n and sizes[tail_pos + 1] == sizes[start]:
            tail_pos += 1
        if tail_pos == start:
            return None
        for i in range(start, tail_pos + 1):
            order[i] = start + 1 + (i - start + 1) % (tail_pos - start + 1)
        start = tail_pos + 1
    return order


# --- clause: main :: () -> None ---
def main():
    out = []
    for sizes in read_input():
        order = shuffle_shoes(sizes)
        if order is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
