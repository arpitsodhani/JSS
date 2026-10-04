import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: build_partition :: (a: list[int]) -> list[tuple[int, int]] | None ---
def build_partition(a):
    n = len(a)
    if n % 2:
        return None
    pieces = []
    spot = 0
    while spot < n:
        if a[spot] + a[spot + 1] == 0:
            pieces.append((spot + 1, spot + 1))
            pieces.append((spot + 2, spot + 2))
        else:
            pieces.append((spot + 1, spot + 2))
        spot += 2
    return pieces


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        pieces = build_partition(a)
        if pieces is None:
            out.append("-1")
            continue
        out.append(str(len(pieces)))
        for low, high in pieces:
            out.append("%d %d" % (low, high))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
