import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 3 * i], fields[2 + 3 * i], fields[3 + 3 * i]))
    return cases


# --- clause: better_elevator :: (a: int, b: int, c: int) -> int ---
def better_elevator(a, b, c):
    lead = a - 1
    next_value = abs(b - c) + c - 1
    if lead < next_value:
        return 1
    if next_value < lead:
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
