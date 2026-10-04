import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 3 * i], tokens[2 + 3 * i], tokens[3 + 3 * i]))
    return cases


# --- clause: better_elevator :: (a: int, b: int, c: int) -> int ---
def better_elevator(a, b, c):
    first = a - 1
    two = abs(b - c) + c - 1
    if first < two:
        return 1
    if two < first:
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
