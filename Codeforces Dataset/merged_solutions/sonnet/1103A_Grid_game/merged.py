import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()

# Clause place_tiles [Confidence: 1.00]
def place_tiles(tiles):
    across = 0
    down = 0
    out = []
    for kind in tiles:
        if kind == "1":
            out.append("1 %d" % (1 + 2 * across))
            across = (across + 1) % 2
        else:
            out.append("3 %d" % (1 + down))
            down = (down + 1) % 4
    return out

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("\n".join(place_tiles(read_input())) + "\n")


if __name__ == "__main__":
    main()

