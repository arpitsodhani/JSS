import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: paint_board :: (n: int, m: int) -> list[str] ---
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, m in read_input():
        lines.extend(paint_board(n, m))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
