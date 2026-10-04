import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n, m, k = map(int, data[:3])

    cells = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            for j in range(1, m + 1):
                cells.append((i, j))
        else:
            for j in range(m, 0, -1):
                cells.append((i, j))

    idx = 0
    out = []

    for _ in range(k - 1):
        group = cells[idx:idx + 2]
        idx += 2
        line = [str(len(group))]
        for x, y in group:
            line.append(str(x))
            line.append(str(y))
        out.append(" ".join(line))

    group = cells[idx:]
    line = [str(len(group))]
    for x, y in group:
        line.append(str(x))
        line.append(str(y))
    out.append(" ".join(line))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
