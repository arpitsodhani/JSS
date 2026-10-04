import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 3 * i], fields[2 + 3 * i], fields[3 + 3 * i]))
    return cases


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: widest_pair :: (l: int, r: int, g: int) -> tuple[int, int] ---
def widest_pair(l, r, g):
    lower = (l + g - 1) // g
    large = r // g
    if lower > large:
        return -1, -1
    span = large - lower
    while span >= 0:
        start = lower
        while start + span <= large:
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
