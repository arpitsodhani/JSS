import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 3 * i], numbers[2 + 3 * i], numbers[3 + 3 * i]))
    return cases


# --- clause: fewest_cups :: (h: int, c: int, t: int) -> int ---
def fewest_cups(h, c, t):
    if 2 * t <= h + c:
        return 2
    low = 0
    high = 1000000
    while low + 1 < high:
        mid = (low + high) // 2
        if (mid + 1) * h + mid * c > t * (2 * mid + 1):
            low = mid
        else:
            high = mid
    best = 1
    gap = None
    for k in (low, low + 1, high, 0):
        if k < 0:
            continue
        cups = 2 * k + 1
        diff = abs((k + 1) * h + k * c - t * cups)
        if gap is None or diff * best < gap * cups:
            gap = diff
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
