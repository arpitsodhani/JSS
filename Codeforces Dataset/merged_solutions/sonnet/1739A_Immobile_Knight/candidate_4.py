import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(t)]


# --- clause: find_cell :: (n: int, m: int) -> tuple[int, int] ---
def find_cell(n, m):
    if n <= 2 or m <= 2:
        if n == 1 or m == 1:
            return 1, 1
        if n == 2 and m == 2:
            return 1, 1
    row = 1
    while row <= n:
        column = 1
        while column <= m:
            moves = 0
            for dr in (-2, -1, 1, 2):
                for dc in (-2, -1, 1, 2):
                    if abs(dr) + abs(dc) != 3:
                        continue
                    if 1 <= row + dr <= n and 1 <= column + dc <= m:
                        moves += 1
            if moves == 0:
                return row, column
            column += 1
        row += 1
    return 1, 1


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m in read_input():
        record, column = find_cell(n, m)
        out.append("%d %d" % (record, column))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
