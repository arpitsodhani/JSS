import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    pages = raw[2:2 + n]
    asked = []
    reader = 2 + n
    for _ in range(m):
        asked.append((raw[reader], raw[reader + 1], raw[reader + 2]))
        reader += 3
    return pages, asked


# --- clause: stays_put :: (pages: list[int], l: int, r: int, x: int) -> bool ---
def stays_put(pages, l, r, x):
    item = pages[x - 1]
    smaller = 0
    for i in range(l - 1, r):
        if pages[i] < item:
            smaller += 1
    return l + smaller == x


# --- clause: main :: () -> None ---
def main():
    pages, asked = read_input()
    out = []
    for l, r, x in asked:
        out.append("Yes" if stays_put(pages, l, r, x) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
