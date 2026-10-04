import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    return x, data[2:2 + n]


# --- clause: best_beauty :: (x: int, a: list[int]) -> int ---
def best_beauty(x, a):
    before = 0
    inside = 0
    after = 0
    best = 0
    for value in a:
        plain = before + value
        if plain < 0:
            plain = 0
        base = before if before > inside else inside
        scaled = base + value * x
        if scaled < 0:
            scaled = 0
        tail = (after if after > inside else inside) + value
        if tail < 0:
            tail = 0
        before = plain
        inside = scaled
        after = tail
        here = before
        if inside > here:
            here = inside
        if after > here:
            here = after
        if here > best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(x, a))


if __name__ == "__main__":
    main()
