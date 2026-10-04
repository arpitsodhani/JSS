import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
    return cases


# --- clause: paint_board :: (n: int, m: int) -> list[str] ---
def paint_board(n, m):
    rows = ["W" + "B" * (m - 1)]
    for _ in range(n - 1):
        rows.append("B" * m)
    return rows


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n, m in read_input():
        collected.extend(paint_board(n, m))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
