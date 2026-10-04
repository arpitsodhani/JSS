import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    values = list(map(int, data[:2]))
    return values[0], values[1]


# --- clause: build_sets :: (n: int, k: int) -> list[str] ---
def build_sets(n, k):
    out = []
    for i in range(n):
        base = 6 * i + 1
        picks = (base, base + 1, base + 2, base + 4)
        parts = []
        for value in picks:
            parts.append(str(k * value))
        out.append(" ".join(parts))
    return out


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    lines = [str(k * (6 * n - 1))]
    lines.extend(build_sets(n, k))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
