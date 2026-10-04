import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    pos = 1
    while len(cases) < q:
        cases.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2])))
        pos += 3
    return cases


# --- clause: closest_total :: (a: int, b: int, c: int) -> int ---
def closest_total(a, b, c):
    low = a
    high = a
    for value in (b, c):
        if value < low:
            low = value
        if value > high:
            high = value
    spread = high - low
    if spread <= 2:
        return 0
    return 2 * (spread - 2)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(closest_total(a, b, c)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
