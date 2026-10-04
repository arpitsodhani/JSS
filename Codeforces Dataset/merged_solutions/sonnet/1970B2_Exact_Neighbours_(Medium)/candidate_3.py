# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def free_column(taken, n):
    c = 1
    while c <= n:
        if not taken[c]:
            return c
        c += 1
    return -1

def place_with_column(points, limit, col, dist, n):
    for j in range(1, limit):
        x, y = points[j]
        vertical = dist - abs(col - x)
        if vertical < 0:
            continue
        up = y + vertical
        if 1 <= up <= n:
            return j, up
        down = y - vertical
        if 1 <= down <= n:
            return j, down
    return -1, -1

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    arr = [0] + [int(v) for v in data[1:1 + n]]
    points = [(0, 0)] * (n + 1)
    target = [1] * (n + 1)
    taken = [False] * (n + 1)
    points[1] = (1, 1)
    taken[1] = True
    for i in range(2, n + 1):
        dist = arr[i]
        if dist == 0:
            print("NO")
            return
        direct = dist + 1
        if direct <= n and not taken[direct]:
            points[i] = (direct, 1)
            target[i] = 1
            taken[direct] = True
        else:
            col = free_column(taken, n)
            if col == -1:
                print("NO")
                return
            parent, row = place_with_column(points, i, col, dist, n)
            if parent == -1:
                print("NO")
                return
            points[i] = (col, row)
            target[i] = parent
            taken[col] = True
    lines = ["YES"]
    for x, y in points[1:]:
        lines.append(f"{x} {y}")
    lines.append(" ".join(str(x) for x in target[1:]))
    print("\n".join(lines))

# CLAUSE: finish_program
main()
