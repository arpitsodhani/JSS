import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return cases


# --- clause: fewest_cups :: (h: int, c: int, t: int) -> int ---
def fewest_cups(h, c, t):
    if 2 * t <= h + c:
        return 2
    floor_value = 0
    top_value = 1000000
    while floor_value < top_value:
        mid = (floor_value + top_value) // 2
        if (mid + 1) * h + mid * c <= t * (2 * mid + 1):
            top_value = mid
        else:
            floor_value = mid + 1
    best = 2 * floor_value + 1
    gap = None
    for k in (floor_value - 1, floor_value, floor_value + 1):
        if k < 0:
            continue
        cups = 2 * k + 1
        top = (k + 1) * h + k * c - t * cups
        if top < 0:
            top = -top
        if gap is None or top * best < gap * cups:
            gap = top
            best = cups
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for h, c, t in read_input():
        out.append(fewest_cups(h, c, t))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
