import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: build_data :: (n: int, k: int) -> list[tuple[int, int]] | None ---
def build_data(n, k):
    comparisons = n * (n - 1) // 2
    if comparisons <= k:
        return None
    points = []
    for y in range(n):
        points.append((0, y))
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
