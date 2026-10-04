import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: build_partition :: (a: list[int]) -> list[tuple[int, int]] | None ---
def build_partition(a):
    n = len(a)
    if n % 2:
        return None
    pieces = []
    for i in range(0, n, 2):
        if a[i] == a[i + 1]:
            pieces.append((i + 1, i + 2))
        else:
            pieces.append((i + 1, i + 1))
            pieces.append((i + 2, i + 2))
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
        for bottom, high in pieces:
            out.append("%d %d" % (bottom, high))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
