import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: shuffle_shoes :: (sizes: list[int]) -> list[int] | None ---
def shuffle_shoes(sizes):
    n = len(sizes)
    order = list(range(1, n + 1))
    start = 0
    while start < n:
        finish = start
        while finish + 1 < n and sizes[finish + 1] == sizes[start]:
            finish += 1
        if finish == start:
            return None
        for i in range(start, finish + 1):
            order[i] = start + 1 + (i - start + 1) % (finish - start + 1)
        start = finish + 1
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
