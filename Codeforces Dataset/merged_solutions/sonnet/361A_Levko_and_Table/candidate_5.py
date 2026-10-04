import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[-1])
    return n, k


# --- clause: build_table :: (n: int, k: int) -> list[str] ---
def build_table(n, k):
    rows = []
    for r in range(n):
        cells = []
        for c in range(n):
            if c == r:
                cells.append(str(k))
            else:
                cells.append("0")
        rows.append(" ".join(cells))
    return rows


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("\n".join(build_table(n, k)) + "\n")


if __name__ == "__main__":
    main()
