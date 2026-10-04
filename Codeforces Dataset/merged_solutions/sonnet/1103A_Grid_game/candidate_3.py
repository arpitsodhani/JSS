import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    tiles = data[0].decode()
    return tiles


# --- clause: place_tiles :: (tiles: str) -> list[str] ---
def place_tiles(tiles):
    across = 0
    down = 0
    out = []
    for kind in tiles:
        if kind == "1":
            out.append("1 %d" % (1 + 2 * across))
            across ^= 1
        else:
            out.append("3 %d" % (1 + down))
            down = (down + 1) % 4
    return out


# --- clause: main :: () -> None ---
def main():
    print("\n".join(place_tiles(read_input())))


if __name__ == "__main__":
    main()
