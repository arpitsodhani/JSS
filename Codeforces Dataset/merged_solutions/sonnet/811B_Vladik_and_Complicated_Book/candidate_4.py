import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    pages = numbers[2:2 + n]
    asked = []
    cursor = 2 + n
    for _ in range(m):
        asked.append((numbers[cursor], numbers[cursor + 1], numbers[cursor + 2]))
        cursor += 3
    return pages, asked


# --- clause: stays_put :: (pages: list[int], l: int, r: int, x: int) -> bool ---
def stays_put(pages, l, r, x):
    value = pages[x - 1]
    spot = l
    for i in range(l - 1, r):
        if pages[i] < value:
            spot += 1
        if spot > x:
            return False
    return spot == x


# --- clause: main :: () -> None ---
def main():
    pages, asked = read_input()
    out = []
    for l, r, x in asked:
        out.append("Yes" if stays_put(pages, l, r, x) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
