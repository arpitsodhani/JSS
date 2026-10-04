import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    d = int(data[1])
    xs = list(map(int, data[2:2 + n]))
    return n, d, xs


# --- clause: count_triples :: (n: int, d: int, xs: list[int]) -> int ---
def count_triples(n, d, xs):
    total = 0
    left = 0
    for right in range(n):
        limit = xs[right] - d
        while xs[left] < limit:
            left += 1
        pairs = right - left
        total += pairs * (pairs - 1) // 2
    return total

# --- clause: main :: () -> None ---
def main():
    n, d, xs = read_input()
    sys.stdout.write(str(count_triples(n, d, xs)) + "\n")


if __name__ == "__main__":
    main()
