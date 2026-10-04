import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    for i in range(q):
        cases.append((int(data[3 * i + 1]), int(data[3 * i + 2]), int(data[3 * i + 3])))
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
    spread = high - low - 2
    if spread < 0:
        spread = 0
    return 2 * spread


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(closest_total(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
