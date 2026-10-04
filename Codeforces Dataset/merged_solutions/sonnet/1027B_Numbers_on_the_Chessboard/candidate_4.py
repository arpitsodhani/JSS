import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    q = numbers[1]
    asked = []
    for i in range(q):
        asked.append((numbers[2 + 2 * i], numbers[3 + 2 * i]))
    return n, asked


# --- clause: cell_value :: (n: int, x: int, y: int) -> int ---
def cell_value(n, x, y):
    even_rows = (x - 1) // 2
    odd_rows = x - 1 - even_rows
    wide = (n + 1) // 2
    narrow = n // 2
    if (x + y) % 2 == 0:
        before = odd_rows * wide + even_rows * narrow
        inside = (y + 1) // 2 if x % 2 else y // 2
        return before + inside
    before = odd_rows * narrow + even_rows * wide
    inside = y // 2 if x % 2 else (y + 1) // 2
    return (n * n + 1) // 2 + before + inside


# --- clause: main :: () -> None ---
def main():
    n, asked = read_input()
    pieces = []
    for x, y in asked:
        pieces.append(cell_value(n, x, y))
    sys.stdout.write("\n".join(map(str, pieces)) + "\n")


if __name__ == "__main__":
    main()
