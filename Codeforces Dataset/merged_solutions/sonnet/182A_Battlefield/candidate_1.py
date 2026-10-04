import sys


# --- clause: read_input :: () -> tuple[int, int, tuple, tuple, list] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    a = data[0]
    b = data[1]
    start = (data[2], data[3])
    goal = (data[4], data[5])
    n = data[6]
    trenches = []
    pos = 7
    for _ in range(n):
        trenches.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return a, b, start, goal, trenches


# --- clause: point_gap :: (px: int, py: int, seg: tuple) -> float ---
def point_gap(px, py, seg):
    x1, y1, x2, y2 = seg
    dx = x2 - x1
    dy = y2 - y1
    span = dx * dx + dy * dy
    if span == 0:
        share = 0.0
    else:
        share = ((px - x1) * dx + (py - y1) * dy) / span
        if share < 0.0:
            share = 0.0
        elif share > 1.0:
            share = 1.0
    cx = x1 + share * dx
    cy = y1 + share * dy
    return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5


# --- clause: segment_gap :: (first: tuple, second: tuple) -> float ---
def segment_gap(first, second):
    best = point_gap(first[0], first[1], second)
    here = point_gap(first[2], first[3], second)
    if here < best:
        best = here
    here = point_gap(second[0], second[1], first)
    if here < best:
        best = here
    here = point_gap(second[2], second[3], first)
    if here < best:
        best = here
    return best


# --- clause: shortest_time :: (a: int, b: int, start: tuple, goal: tuple, trenches: list) -> float ---
def shortest_time(a, b, start, goal, trenches):
    straight = ((start[0] - goal[0]) ** 2 + (start[1] - goal[1]) ** 2) ** 0.5
    if straight <= a:
        return straight
    n = len(trenches)
    level = [-1] * n
    queue = []
    for i in range(n):
        if point_gap(start[0], start[1], trenches[i]) <= a:
            level[i] = 0
            queue.append(i)
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        for other in range(n):
            if level[other] < 0 and segment_gap(trenches[node], trenches[other]) <= a:
                level[other] = level[node] + 1
                queue.append(other)
    best = -1.0
    for i in range(n):
        if level[i] < 0:
            continue
        reach = point_gap(goal[0], goal[1], trenches[i])
        if reach <= a:
            total = (level[i] + 1) * (a + b) + reach
            if best < 0 or total < best:
                best = total
    return best


# --- clause: main :: () -> None ---
def main():
    a, b, start, goal, trenches = read_input()
    answer = shortest_time(a, b, start, goal, trenches)
    if answer < 0:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("%.10f\n" % answer)


if __name__ == "__main__":
    main()
