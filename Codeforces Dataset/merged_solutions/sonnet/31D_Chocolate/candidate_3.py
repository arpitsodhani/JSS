import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    width = int(data[0])
    height = int(data[1])
    n = int(data[2])
    cuts = []
    pos = 3
    while len(cuts) < n:
        cuts.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2]), int(data[pos + 3])))
        pos += 4
    return width, height, n, cuts


# --- clause: build_walls :: (width: int, height: int, cuts: list) -> tuple[list, list] ---
def build_walls(width, height, cuts):
    vertical = [[False] * height for _ in range(width + 1)]
    horizontal = [[False] * (height + 1) for _ in range(width)]
    for x1, y1, x2, y2 in cuts:
        if x1 == x2:
            for y in range(y1, y2):
                vertical[x1][y] = True
        else:
            for x in range(x1, x2):
                horizontal[x][y1] = True
    return vertical, horizontal


# --- clause: piece_areas :: (width: int, height: int, vertical: list, horizontal: list) -> list[int] ---
def piece_areas(width, height, vertical, horizontal):
    seen = [[False] * height for _ in range(width)]
    areas = []
    for sx in range(width):
        for sy in range(height):
            if seen[sx][sy]:
                continue
            seen[sx][sy] = True
            queue = [(sx, sy)]
            head = 0
            while head < len(queue):
                x, y = queue[head]
                head += 1
                if x > 0 and not vertical[x][y] and not seen[x - 1][y]:
                    seen[x - 1][y] = True
                    queue.append((x - 1, y))
                if x + 1 < width and not vertical[x + 1][y] and not seen[x + 1][y]:
                    seen[x + 1][y] = True
                    queue.append((x + 1, y))
                if y > 0 and not horizontal[x][y] and not seen[x][y - 1]:
                    seen[x][y - 1] = True
                    queue.append((x, y - 1))
                if y + 1 < height and not horizontal[x][y + 1] and not seen[x][y + 1]:
                    seen[x][y + 1] = True
                    queue.append((x, y + 1))
            areas.append(head)
    areas.sort()
    return areas


# --- clause: main :: () -> None ---
def main():
    width, height, n, cuts = read_input()
    vertical, horizontal = build_walls(width, height, cuts)
    areas = piece_areas(width, height, vertical, horizontal)
    print(" ".join(map(str, areas)))


if __name__ == "__main__":
    main()
