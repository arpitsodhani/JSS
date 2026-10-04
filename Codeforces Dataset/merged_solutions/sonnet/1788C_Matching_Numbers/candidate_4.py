import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_pairs :: (n: int) -> list[tuple[int, int]] | None ---
def build_pairs(n):
    if n % 2 == 0:
        return None
    k = (n - 1) // 2
    pairs = []
    i = 1
    while i <= k:
        pairs.append((2 * i, 2 * n - k - i))
        i += 1
    i = 1
    while i <= k + 1:
        pairs.append((2 * i - 1, 2 * n + 1 - i))
        i += 1
    return pairs


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pairs = build_pairs(n)
        if pairs is None:
            pieces.append("No")
        else:
            pieces.append("Yes")
            for a, b in pairs:
                pieces.append("%d %d" % (a, b))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
