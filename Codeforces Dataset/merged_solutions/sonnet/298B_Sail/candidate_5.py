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
    step = {"E": (1, 0), "W": (-1, 0), "N": (0, 1), "S": (0, -1)}
    for second, gust in enumerate(wind, start=1):
        mx, my = step[gust]
        if mx and mx * dx > 0:
            dx -= mx
        elif my and my * dy > 0:
            dy -= my
        if dx == 0 and dy == 0:
            return second
    return -1

# --- clause: main :: () -> None ---
def main():
    t, sx, sy, ex, ey, wind = read_input()
    sys.stdout.write(str(earliest_arrival(t, sx, sy, ex, ey, wind)) + "\n")


if __name__ == "__main__":
    main()
