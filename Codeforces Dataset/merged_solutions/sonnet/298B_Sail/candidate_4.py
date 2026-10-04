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
    need_x = ex - sx
    need_y = ey - sy
    second = 0
    while second < t:
        gust = wind[second]
        second += 1
        if gust == "E":
            if need_x > 0:
                need_x -= 1
        elif gust == "W":
            if need_x < 0:
                need_x += 1
        elif gust == "N":
            if need_y > 0:
                need_y -= 1
        elif need_y < 0:
            need_y += 1
        if need_x == 0 and need_y == 0:
            return second
    return -1

# --- clause: main :: () -> None ---
def main():
    t, sx, sy, ex, ey, wind = read_input()
    sys.stdout.write(str(earliest_arrival(t, sx, sy, ex, ey, wind)) + "\n")


if __name__ == "__main__":
    main()
