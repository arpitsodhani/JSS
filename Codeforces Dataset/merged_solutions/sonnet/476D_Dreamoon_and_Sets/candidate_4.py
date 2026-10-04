import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[-1])


# --- clause: build_sets :: (n: int, k: int) -> list[str] ---
def build_sets(n, k):
    out = []
    for i in range(n):
        base = 6 * i + 1
        picks = (base, 1 + base, 2 + base, 4 + base)
        out.append(" ".join(str(k * value) for value in picks))
    return out


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    lines = [str((6 * n - 1) * k)]
    for row in build_sets(n, k):
        lines.append(row)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
