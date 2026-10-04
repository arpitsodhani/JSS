import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: build_data :: (n: int, k: int) -> list[tuple[int, int]] | None ---
def build_data(n, k):
    pairs = n * (n - 1) // 2
    if pairs <= k:
        return None
    points = []
    y = 0
    while y < n:
        points.append((0, 2 * y))
        y += 1
    return points


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    points = build_data(n, k)
    if points is None:
        sys.stdout.write("no solution\n")
    else:
        sys.stdout.write("\n".join("%d %d" % p for p in points) + "\n")


if __name__ == "__main__":
    main()
