import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return str(data[0], "ascii")


# --- clause: place_tiles :: (tiles: str) -> list[str] ---
def place_tiles(tiles):
    across = 0
    down = 0
    out = []
    for kind in tiles:
        if kind == "0":
            out.append("3 " + str(down + 1))
            down += 1
            if down == 4:
                down = 0
        else:
            out.append("1 " + str(2 * across + 1))
            across += 1
            if across == 2:
                across = 0
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % "\n".join(place_tiles(read_input())))


if __name__ == "__main__":
    main()
