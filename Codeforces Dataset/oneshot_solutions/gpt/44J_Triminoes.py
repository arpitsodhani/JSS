import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    a = [list(data[i + 2]) for i in range(n)]

    letters = "abcd"
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def fail():
        print("NO")
        sys.exit(0)

    def choose(cells):
        used = set()
        for x, y in cells:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] in letters:
                    used.add(a[nx][ny])
        for ch in letters:
            if ch not in used:
                return ch
        return None

    for i in range(n):
        for j in range(m):
            if a[i][j] == 'b':
                fail()
            if a[i][j] != 'w':
                continue

            cells = None
            if j + 2 < m and a[i][j + 1] == 'b' and a[i][j + 2] == 'w':
                cells = [(i, j), (i, j + 1), (i, j + 2)]
            elif i + 2 < n and a[i + 1][j] == 'b' and a[i + 2][j] == 'w':
                cells = [(i, j), (i + 1, j), (i + 2, j)]
            else:
                fail()

            ch = choose(cells)
            if ch is None:
                fail()
            for x, y in cells:
                a[x][y] = ch

    print("YES")
    print("\n".join("".join(row) for row in a))

if __name__ == "__main__":
    main()
