import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    return n, k


# --- clause: build_table :: (n: int, k: int) -> list[str] ---
def build_table(n, k):
    rows = []
    for r in range(n):
        cells = []
        for c in range(n):
            if r != c:
                cells.append("0")
            else:
                cells.append(str(k))
        rows.append(" ".join(cells))
    return rows


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%s\n" % "\n".join(build_table(n, k)))


if __name__ == "__main__":
    main()
