import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0].decode())
    k = int(data[1])
    return n, k


# --- clause: build_table :: (n: int, k: int) -> list[str] ---
def build_table(n, k):
    rows = []
    peak = str(k)
    for r in range(n):
        cells = ["0"] * n
        cells[r] = peak
        rows.append(" ".join(cells))
    return rows


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    print("\n".join(build_table(n, k)))


if __name__ == "__main__":
    main()
