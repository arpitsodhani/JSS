import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sx = int(data[1])
    sy = int(data[2])
    ex = int(data[3])
    ey = int(data[4])
    return t, sx, sy, ex, ey, data[5].decode()

# --- clause: earliest_arrival :: (t: int, sx: int, sy: int, ex: int, ey: int, wind: str) -> int ---
def earliest_arrival(t, sx, sy, ex, ey, wind):
    east = ex - sx if ex > sx else 0
    west = sx - ex if sx > ex else 0
    north = ey - sy if ey > sy else 0
    south = sy - ey if sy > ey else 0
    for second, gust in enumerate(wind, start=1):
        if gust == "E" and east:
            east -= 1
        elif gust == "W" and west:
            west -= 1
        elif gust == "N" and north:
            north -= 1
        elif gust == "S" and south:
            south -= 1
        if not (east or west or north or south):
            return second
    return -1

# --- clause: main :: () -> None ---
def main():
    t, sx, sy, ex, ey, wind = read_input()
    sys.stdout.write(str(earliest_arrival(t, sx, sy, ex, ey, wind)) + "\n")


if __name__ == "__main__":
    main()
