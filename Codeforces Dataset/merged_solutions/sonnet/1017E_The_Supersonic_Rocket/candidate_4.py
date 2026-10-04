import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    first = []
    for i in range(n):
        first.append((numbers[2 + 2 * i], numbers[3 + 2 * i]))
    pos = 2 + 2 * n
    follow = []
    for i in range(m):
        follow.append((numbers[pos + 2 * i], numbers[pos + 1 + 2 * i]))
    return first, follow


# --- clause: convex_hull :: (points: list[tuple[int, int]]) -> list[tuple[int, int]] ---
def convex_hull(points):
    spots = sorted(set(points))
    if len(spots) <= 2:
        return spots
    lower = []
    for spot in spots:
        while len(lower) >= 2:
            ax, ay = lower[-2]
            bx, by = lower[-1]
            if (bx - ax) * (spot[1] - ay) - (by - ay) * (spot[0] - ax) <= 0:
                lower.pop()
            else:
                break
        lower.append(spot)
    upper = []
    for spot in reversed(spots):
        while len(upper) >= 2:
            ax, ay = upper[-2]
            bx, by = upper[-1]
            if (bx - ax) * (spot[1] - ay) - (by - ay) * (spot[0] - ax) <= 0:
                upper.pop()
            else:
                break
        upper.append(spot)
    return lower[:-1] + upper[:-1]


# --- clause: shape_code :: (hull: list[tuple[int, int]]) -> list[tuple[int, int]] ---
def shape_code(hull):
    size = len(hull)
    code = []
    for i in range(size):
        ax, ay = hull[i]
        bx, by = hull[(i + 1) % size]
        cx, cy = hull[(i + 2) % size]
        first = (bx - ax, by - ay)
        follow = (cx - bx, cy - by)
        length = first[0] * first[0] + first[1] * first[1]
        turn = first[0] * follow[1] - first[1] * follow[0]
        code.append((length, turn))
    return code


# --- clause: same_cycle :: (left: list[tuple[int, int]], right: list[tuple[int, int]]) -> bool ---
def same_cycle(left, right):
    size = len(left)
    if size != len(right):
        return False
    if size == 0:
        return True
    doubled = right + right
    fail = [0] * size
    step = 0
    for i in range(1, size):
        while step and left[i] != left[step]:
            step = fail[step - 1]
        if left[i] == left[step]:
            step += 1
        fail[i] = step
    step = 0
    for i in range(len(doubled)):
        while step and doubled[i] != left[step]:
            step = fail[step - 1]
        if doubled[i] == left[step]:
            step += 1
        if step == size:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    first, follow = read_input()
    left = convex_hull(first)
    right = convex_hull(follow)
    ok = len(left) == len(right) and same_cycle(shape_code(left), shape_code(right))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
