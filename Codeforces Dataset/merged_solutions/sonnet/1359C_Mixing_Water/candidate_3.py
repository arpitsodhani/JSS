import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 3 * i], fields[2 + 3 * i], fields[3 + 3 * i]))
    return cases


# --- clause: fewest_cups :: (h: int, c: int, t: int) -> int ---
def fewest_cups(h, c, t):
    if 2 * t <= h + c:
        return 2
    low = 0
    large = 1000000
    while low < large:
        mid = (low + large) // 2
        if (mid + 1) * h + mid * c <= t * (2 * mid + 1):
            large = mid
        else:
            low = mid + 1
    champion = 2 * low + 1
    gap = None
    for k in (low - 1, low, low + 1):
        if k < 0:
            continue
        cups = 2 * k + 1
        top = (k + 1) * h + k * c - t * cups
        if top < 0:
            top = -top
        if gap is None or top * champion < gap * cups:
            gap = top
            champion = cups
    return champion


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, c, t in read_input():
        out.append(fewest_cups(h, c, t))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
