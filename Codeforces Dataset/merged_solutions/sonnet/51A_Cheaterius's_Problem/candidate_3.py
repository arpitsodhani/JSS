import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    amulets = []
    cursor = 1
    for _ in range(n):
        while fields[cursor] == b"**":
            cursor += 1
        top = fields[cursor].decode()
        bottom = fields[cursor + 1].decode()
        cursor += 2
        amulets.append((int(top[0]), int(top[1]), int(bottom[0]), int(bottom[1])))
    return amulets


# --- clause: canonical :: (amulet: tuple[int, int, int, int]) -> tuple[int, int, int, int] ---
def canonical(amulet):
    champion = amulet
    a, b, c, d = amulet
    for _ in range(3):
        a, b, c, d = c, a, d, b
        if (a, b, c, d) < champion:
            champion = (a, b, c, d)
    return champion


# --- clause: main :: () -> None ---
def main():
    piles = set()
    for amulet in read_input():
        piles.add(canonical(amulet))
    sys.stdout.write("%d\n" % len(piles))


if __name__ == "__main__":
    main()
