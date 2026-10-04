import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    first = []
    for i in range(n):
        first.append((data[2 + 2 * i], data[3 + 2 * i]))
    pos = 2 + 2 * n
    second = []
    for i in range(m):
        second.append((data[pos + 2 * i], data[pos + 1 + 2 * i]))
    return first, second

# Clause convex_hull [Confidence: 1.00]
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

# Clause shape_code [Confidence: 1.00]
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

# Clause same_cycle [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    first, follow = read_input()
    left = convex_hull(first)
    right = convex_hull(follow)
    ok = len(left) == len(right) and same_cycle(shape_code(left), shape_code(right))
    sys.stdout.write("YES\n" if ok else "NO\n")


if __name__ == "__main__":
    main()

