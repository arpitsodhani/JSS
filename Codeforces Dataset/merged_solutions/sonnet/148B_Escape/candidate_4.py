import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]


# --- clause: count_bijous :: (vp: int, vd: int, t: int, f: int, c: int) -> int ---
def count_bijous(vp, vd, t, f, c):
    if vp >= vd:
        return 0
    ratio = vd / float(vd - vp)
    place = float(vp * t)
    used = 0
    while place * ratio < c:
        meet = place * ratio
        place = meet + vp * (meet / float(vd) + f)
        used += 1
    return used


# --- clause: main :: () -> None ---
def main():
    vp, vd, t, f, c = read_input()
    sys.stdout.write("%d\n" % count_bijous(vp, vd, t, f, c))


if __name__ == "__main__":
    main()
