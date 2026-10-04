import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return cases


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: widest_pair :: (l: int, r: int, g: int) -> tuple[int, int] ---
def widest_pair(l, r, g):
    floor_value = (l + g - 1) // g
    top_value = r // g
    if floor_value > top_value:
        return -1, -1
    span = top_value - floor_value
    while span >= 0:
        start = floor_value
        while start + span <= top_value:
            if gcd_of(start, start + span) == 1:
                return start * g, (start + span) * g
            start += 1
        span -= 1
    return -1, -1


# --- clause: main :: () -> None ---
def main():
    out = []
    for l, r, g in read_input():
        out.append("%d %d" % widest_pair(l, r, g))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
