import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2], tokens[3], tokens[4]


# --- clause: count_bijous :: (vp: int, vd: int, t: int, f: int, c: int) -> int ---
def count_bijous(vp, vd, t, f, c):
    if vd <= vp:
        return 0
    place = vp * t
    used = 0
    while True:
        meet = place * vd / float(vd - vp)
        if meet >= c:
            return used
        used += 1
        place = meet + vp * (meet / float(vd) + f)


# --- clause: main :: () -> None ---
def main():
    vp, vd, t, f, c = read_input()
    sys.stdout.write("%d\n" % count_bijous(vp, vd, t, f, c))


if __name__ == "__main__":
    main()
