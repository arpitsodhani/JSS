import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int]], list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    first = []
    for i in range(n):
        first.append((raw[2 + 2 * i], raw[3 + 2 * i]))
    reader = 2 + 2 * n
    secondary = []
    for i in range(m):
        secondary.append((raw[reader + 2 * i], raw[reader + 1 + 2 * i]))
    return first, secondary


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
        secondary = (cx - bx, cy - by)
        length = first[0] * first[0] + first[1] * first[1]
        turn = first[0] * secondary[1] - first[1] * secondary[0]
        code.append((length, turn))
    return code


# --- clause: same_cycle :: (left: list[tuple[int, int]], right: list[tuple[int, int]]) -> bool ---
def same_cycle(left, right):
    if len(left) != len(right):
        return False
    if not left:
        return True
    pattern = left + [(-1, -1)] + right + right
    fail = [0] * len(pattern)
    for i in range(1, len(pattern)):
        step = fail[i - 1]
        while step and pattern[i] != pattern[step]:
            step = fail[step - 1]
        if pattern[i] == pattern[step]:
            step += 1
        fail[i] = step
        if step == len(left):
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    first, secondary = read_input()
    left = convex_hull(first)
    right = convex_hull(secondary)
    ok = len(left) == len(right) and same_cycle(shape_code(left), shape_code(right))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()
