import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i], raw[2 + 3 * i], raw[3 + 3 * i]))
    return cases


# --- clause: better_elevator :: (a: int, b: int, c: int) -> int ---
def better_elevator(a, b, c):
    first = a - 1
    secondary = abs(b - c) + c - 1
    if first < secondary:
        return 1
    if secondary < first:
        return 2
    return 3


# --- clause: main :: () -> None ---
def main():
    written = []
    for a, b, c in read_input():
        written.append(better_elevator(a, b, c))
    sys.stdout.write("\n".join(map(str, written)) + "\n")


if __name__ == "__main__":
    main()
