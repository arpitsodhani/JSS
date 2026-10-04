import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    amulets = []
    pos = 1
    for _ in range(n):
        while tokens[pos] == b"**":
            pos += 1
        top = tokens[pos].decode()
        bottom = tokens[pos + 1].decode()
        pos += 2
        amulets.append((int(top[0]), int(top[1]), int(bottom[0]), int(bottom[1])))
    return amulets


# --- clause: canonical :: (amulet: tuple[int, int, int, int]) -> tuple[int, int, int, int] ---
def canonical(amulet):
    finest = amulet
    a, b, c, d = amulet
    for _ in range(3):
        a, b, c, d = c, a, d, b
        if (a, b, c, d) < finest:
            finest = (a, b, c, d)
    return finest


# --- clause: main :: () -> None ---
def main():
    piles = set()
    for amulet in read_input():
        piles.add(canonical(amulet))
    sys.stdout.write("%d\n" % len(piles))


if __name__ == "__main__":
    main()
