import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    return n, k


# --- clause: build_sets :: (n: int, k: int) -> list[str] ---
def build_sets(n, k):
    out = []
    base = 1
    while base <= 6 * n:
        picks = [base, base + 1, base + 2, base + 4]
        out.append(" ".join(str(k * value) for value in picks))
        base += 6
    return out


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    lines = [str(k * (6 * n - 1))]
    lines.extend(build_sets(n, k))
    sys.stdout.write("%s\n" % "\n".join(lines))


if __name__ == "__main__":
    main()
