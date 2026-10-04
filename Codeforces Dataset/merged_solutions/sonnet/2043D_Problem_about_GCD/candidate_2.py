import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 3 * i], tokens[2 + 3 * i], tokens[3 + 3 * i]))
    return cases


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: widest_pair :: (l: int, r: int, g: int) -> tuple[int, int] ---
def widest_pair(l, r, g):
    bottom = (l + g - 1) // g
    high = r // g
    if bottom > high:
        return -1, -1
    span = high - bottom
    while span >= 0:
        start = bottom
        while start + span <= high:
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
