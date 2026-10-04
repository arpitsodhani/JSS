import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    return [tuple(data[1 + 5 * i:6 + 5 * i]) for i in range(t)]


# --- clause: is_possible :: (n: int, a: int, b: int, c: int, d: int) -> bool ---
def is_possible(n, a, b, c, d):
    low = n * (a - b)
    high = n * (a + b)
    return low <= c + d and c - d <= high


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, b, c, d in read_input():
        out.append("Yes" if is_possible(n, a, b, c, d) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
