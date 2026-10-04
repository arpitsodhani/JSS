import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return cases


# --- clause: smallest_total :: (x1: int, x2: int, x3: int) -> int ---
def smallest_total(x1, x2, x3):
    floor_value = x1
    upper = x1
    for value in (x2, x3):
        if value < floor_value:
            floor_value = value
        if value > upper:
            upper = value
    return upper - floor_value


# --- clause: main :: () -> None ---
def main():
    out = []
    for x1, x2, x3 in read_input():
        out.append(smallest_total(x1, x2, x3))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
