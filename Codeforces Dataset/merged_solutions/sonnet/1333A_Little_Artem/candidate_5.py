import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: paint_board :: (n: int, m: int) -> list[str] ---
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows


# --- clause: main :: () -> None ---
def main():
    written = []
    for n, m in read_input():
        written.extend(paint_board(n, m))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
