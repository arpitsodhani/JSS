import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
    return cases


# --- clause: better_elevator :: (a: int, b: int, c: int) -> int ---
def better_elevator(a, b, c):
    first = a - 1
    second = abs(b - c) + c - 1
    if first < second:
        return 1
    if second < first:
        return 2
    return 3


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append(better_elevator(a, b, c))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
