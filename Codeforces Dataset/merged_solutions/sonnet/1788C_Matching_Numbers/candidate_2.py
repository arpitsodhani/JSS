import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


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
    lines = []
    for n in read_input():
        pairs = build_pairs(n)
        if pairs is None:
            lines.append("No")
        else:
            lines.append("Yes")
            for a, b in pairs:
                lines.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
