import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()


# --- clause: place_tiles :: (tiles: str) -> list[str] ---
def place_tiles(tiles):
    out = []
    across = 0
    down = 0
    for kind in tiles:
        if kind == "1":
            out.append("1 %d" % (1 + 2 * across))
            across = (across + 1) % 2
        else:
            out.append("3 %d" % (down + 1))
            down = (down + 1) & 3
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(place_tiles(read_input())) + "\n")


if __name__ == "__main__":
    main()
