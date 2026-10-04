import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: three_parts :: (n: int) -> tuple[int, int, int] ---
def three_parts(n):
    if n % 2:
        return 1, (n - 1) // 2, (n - 1) // 2
    if n % 4 == 0:
        return n // 2, n // 4, n // 4
    return 2, (n - 2) // 2, (n - 2) // 2


# --- clause: split_parts :: (n: int, k: int) -> list[int] ---
def split_parts(n, k):
    parts = [1] * (k - 3)
    return parts + list(three_parts(n - (k - 3)))


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n, k in read_input():
        collected.append(" ".join(map(str, split_parts(n, k))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
