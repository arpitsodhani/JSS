import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    amulets = []
    pos = 1
    for _ in range(n):
        while data[pos] == b"**":
            pos += 1
        top = data[pos].decode()
        bottom = data[pos + 1].decode()
        pos += 2
        amulets.append((int(top[0]), int(top[1]), int(bottom[0]), int(bottom[1])))
    return amulets


# --- clause: canonical :: (amulet: tuple[int, int, int, int]) -> tuple[int, int, int, int] ---
def canonical(amulet):
    best = amulet
    a, b, c, d = amulet
    for _ in range(3):
        a, b, c, d = c, a, d, b
        if (a, b, c, d) < best:
            best = (a, b, c, d)
    return best


# --- clause: main :: () -> None ---
def main():
    piles = set()
    for amulet in read_input():
        piles.add(canonical(amulet))
    sys.stdout.write("%d\n" % len(piles))


if __name__ == "__main__":
    main()
