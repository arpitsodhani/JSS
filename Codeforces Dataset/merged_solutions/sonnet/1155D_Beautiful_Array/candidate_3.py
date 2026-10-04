import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    x = fields[1]
    return x, fields[2:2 + n]


# --- clause: best_beauty :: (x: int, a: list[int]) -> int ---
def best_beauty(x, a):
    before = 0
    inside = 0
    after = 0
    finest = 0
    for element in a:
        plain = before + element
        if plain < 0:
            plain = 0
        base = before if before > inside else inside
        scaled = base + element * x
        if scaled < 0:
            scaled = 0
        tail = (after if after > inside else inside) + element
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
        if here > finest:
            finest = here
    return finest


# --- clause: main :: () -> None ---
def main():
    x, a = read_input()
    sys.stdout.write("%d\n" % best_beauty(x, a))


if __name__ == "__main__":
    main()
