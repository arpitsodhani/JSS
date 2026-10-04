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
    dx = ex - sx
    dy = ey - sy
    for second in range(t):
        gust = wind[second]
        if gust == "E" and dx > 0:
            dx -= 1
        elif gust == "W" and dx < 0:
            dx += 1
        elif gust == "N" and dy > 0:
            dy -= 1
        elif gust == "S" and dy < 0:
            dy += 1
        if dx == 0 and dy == 0:
            return second + 1
    return -1


# --- clause: main :: () -> None ---
def main():
    t, sx, sy, ex, ey, wind = read_input()
    sys.stdout.write(str(earliest_arrival(t, sx, sy, ex, ey, wind)) + "\n")


if __name__ == "__main__":
    main()
