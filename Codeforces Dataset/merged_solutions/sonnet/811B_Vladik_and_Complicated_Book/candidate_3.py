import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    pages = fields[2:2 + n]
    asked = []
    offset = 2 + n
    for _ in range(m):
        asked.append((fields[offset], fields[offset + 1], fields[offset + 2]))
        offset += 3
    return pages, asked


# --- clause: stays_put :: (pages: list[int], l: int, r: int, x: int) -> bool ---
def stays_put(pages, l, r, x):
    entry = pages[x - 1]
    smaller = 0
    for i in range(l - 1, r):
        if pages[i] < entry:
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
