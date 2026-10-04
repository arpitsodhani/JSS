# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def construct(n, a):
    coords = [[0, 0] for _ in range(n + 1)]
    link = [1] * (n + 1)
    occupied = [False] * (n + 1)
    coords[1] = [1, 1]
    occupied[1] = True
    for i, d in enumerate(a[2:], 2):
        if d == 0:
            return None
        col = d + 1
        if col <= n and not occupied[col]:
            coords[i][0] = col
            coords[i][1] = 1
            occupied[col] = True
            link[i] = 1
            continue
        col = next((c for c in range(1, n + 1) if not occupied[c]), 0)
        if col == 0:
            return None
        found = None
        for j in range(1, i):
            px, py = coords[j]
            left = d - abs(col - px)
            if left < 0:
                continue
            rows = (py + left, py - left)
            for row in rows:
                if 1 <= row <= n:
                    found = (j, row)
                    break
            if found is not None:
                break
        if found is None:
            return None
        link[i], coords[i][1] = found
        coords[i][0] = col
        occupied[col] = True
    return coords, link

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    a = [0] + list(map(int, raw[1:1 + n]))
    built = construct(n, a)
    if built is None:
        print("NO")
        return
    coords, link = built
    pieces = ["YES"]
    pieces += ["{} {}".format(coords[i][0], coords[i][1]) for i in range(1, n + 1)]
    pieces.append(" ".join(str(link[i]) for i in range(1, n + 1)))
    print("\n".join(pieces))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
