import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    pages = data[2:2 + n]
    asked = []
    pos = 2 + n
    for _ in range(m):
        asked.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return pages, asked


# --- clause: stays_put :: (pages: list[int], l: int, r: int, x: int) -> bool ---
def stays_put(pages, l, r, x):
    value = pages[x - 1]
    smaller = 0
    for i in range(l - 1, r):
        if pages[i] < value:
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
