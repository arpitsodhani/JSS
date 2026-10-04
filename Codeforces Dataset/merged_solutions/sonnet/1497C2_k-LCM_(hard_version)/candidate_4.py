import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: three_parts :: (n: int) -> tuple[int, int, int] ---
def three_parts(n):
    half = n // 2
    if n % 2 == 1:
        return 1, half, half
    if half % 2 == 0:
        return half, half // 2, half // 2
    return 2, half - 1, half - 1


# --- clause: split_parts :: (n: int, k: int) -> list[int] ---
def split_parts(n, k):
    parts = [1] * (k - 3)
    return parts + list(three_parts(n - (k - 3)))


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, k in read_input():
        pieces.append(" ".join(map(str, split_parts(n, k))))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
