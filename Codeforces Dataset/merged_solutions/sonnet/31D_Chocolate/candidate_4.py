import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[tuple[int, int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    width = int(data[0])
    height = int(data[1])
    n = int(data[2])
    cuts = []
    for i in range(n):
        base = 3 + 4 * i
        cuts.append((int(data[base]), int(data[base + 1]),
                     int(data[base + 2]), int(data[base + 3])))
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
            stack = [(sx, sy)]
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                if x > 0 and not vertical[x][y] and not seen[x - 1][y]:
                    seen[x - 1][y] = True
                    stack.append((x - 1, y))
                if x + 1 < width and not vertical[x + 1][y] and not seen[x + 1][y]:
                    seen[x + 1][y] = True
                    stack.append((x + 1, y))
                if y > 0 and not horizontal[x][y] and not seen[x][y - 1]:
                    seen[x][y - 1] = True
                    stack.append((x, y - 1))
                if y + 1 < height and not horizontal[x][y + 1] and not seen[x][y + 1]:
                    seen[x][y + 1] = True
                    stack.append((x, y + 1))
            areas.append(size)
    return sorted(areas)


# --- clause: main :: () -> None ---
def main():
    width, height, n, cuts = read_input()
    walls = build_walls(width, height, cuts)
    vertical, horizontal = walls[0], walls[1]
    areas = piece_areas(width, height, vertical, horizontal)
    sys.stdout.write(" ".join(map(str, areas)) + "\n")


if __name__ == "__main__":
    main()
