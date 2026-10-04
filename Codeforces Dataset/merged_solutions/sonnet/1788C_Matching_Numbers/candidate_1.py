import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_pairs :: (n: int) -> list[tuple[int, int]] | None ---
def build_pairs(n):
    if n % 2 == 0:
        return None
    k = (n - 1) // 2
    pairs = []
    for i in range(1, k + 2):
        pairs.append((2 * i - 1, 2 * n + 1 - i))
    for i in range(1, k + 1):
        pairs.append((2 * i, 2 * n - k - i))
    return pairs


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        pairs = build_pairs(n)
        if pairs is None:
            out.append("No")
        else:
            out.append("Yes")
            for a, b in pairs:
                out.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
