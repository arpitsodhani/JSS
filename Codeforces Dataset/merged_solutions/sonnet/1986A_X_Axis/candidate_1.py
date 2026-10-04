import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return cases


# --- clause: smallest_total :: (x1: int, x2: int, x3: int) -> int ---
def smallest_total(x1, x2, x3):
    low = x1
    high = x1
    for value in (x2, x3):
        if value < low:
            low = value
        if value > high:
            high = value
    return high - low


# --- clause: main :: () -> None ---
def main():
    out = []
    for x1, x2, x3 in read_input():
        out.append(smallest_total(x1, x2, x3))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
