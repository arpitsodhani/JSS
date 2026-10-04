import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    return [tuple(raw[1 + 5 * i:6 + 5 * i]) for i in range(t)]


# --- clause: is_possible :: (n: int, a: int, b: int, c: int, d: int) -> bool ---
def is_possible(n, a, b, c, d):
    floor_value = n * (a - b)
    top_value = n * (a + b)
    return floor_value <= c + d and c - d <= top_value


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, b, c, d in read_input():
        out.append("Yes" if is_possible(n, a, b, c, d) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
