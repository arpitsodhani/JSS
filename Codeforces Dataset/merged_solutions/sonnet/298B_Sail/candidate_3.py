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
    x = sx
    y = sy
    for second in range(t):
        gust = wind[second]
        if gust == "E":
            if x < ex:
                x += 1
        elif gust == "W":
            if x > ex:
                x -= 1
        elif gust == "N":
            if y < ey:
                y += 1
        else:
            if y > ey:
                y -= 1
        if x == ex and y == ey:
            return second + 1
    return -1

# --- clause: main :: () -> None ---
def main():
    t, sx, sy, ex, ey, wind = read_input()
    sys.stdout.write(str(earliest_arrival(t, sx, sy, ex, ey, wind)) + "\n")


if __name__ == "__main__":
    main()
