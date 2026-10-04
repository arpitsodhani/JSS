import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: shuffle_shoes :: (sizes: list[int]) -> list[int] | None ---
def shuffle_shoes(sizes):
    n = len(sizes)
    order = list(range(1, n + 1))
    start = 0
    while start < n:
        closing = start
        while closing + 1 < n and sizes[closing + 1] == sizes[start]:
            closing += 1
        if closing == start:
            return None
        for i in range(start, closing + 1):
            order[i] = start + 1 + (i - start + 1) % (closing - start + 1)
        start = closing + 1
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
