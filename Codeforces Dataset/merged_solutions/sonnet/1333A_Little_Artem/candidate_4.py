import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: paint_board :: (n: int, m: int) -> list[str] ---
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n, m in read_input():
        pieces.extend(paint_board(n, m))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
