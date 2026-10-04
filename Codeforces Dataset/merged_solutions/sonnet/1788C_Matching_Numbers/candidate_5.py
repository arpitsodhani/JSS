import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


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
    written = []
    for n in read_input():
        pairs = build_pairs(n)
        if pairs is None:
            written.append("No")
        else:
            written.append("Yes")
            for a, b in pairs:
                written.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
