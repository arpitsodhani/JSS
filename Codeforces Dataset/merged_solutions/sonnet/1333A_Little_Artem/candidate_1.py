import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases


# --- clause: paint_board :: (n: int, m: int) -> list[str] ---
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        out.extend(paint_board(n, m))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
