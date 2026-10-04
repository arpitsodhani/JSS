import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return [(raw[1 + 2 * i], raw[2 + 2 * i]) for i in range(n)]


# --- clause: find_clash :: (groups: list[tuple[int, int]], skip: int) -> tuple[int, int] ---
def find_clash(groups, skip):
    queue_order = []
    for i in range(0, len(groups)):
        if i != skip:
            queue_order.append((groups[i][0], groups[i][1], i))
    queue_order.sort()
    for j in range(1, len(queue_order)):
        if queue_order[j][0] < queue_order[j - 1][1]:
            return queue_order[j - 1][2], queue_order[j][2]
    return -1, -1


# --- clause: droppable :: (groups: list[tuple[int, int]]) -> list[int] ---
def droppable(groups):
    a, b = find_clash(groups, -1)
    if a < 0:
        return [i + 1 for i in range(len(groups))]
    lines = []
    for skip in (a, b):
        if find_clash(groups, skip)[0] < 0:
            lines.append(skip + 1)
    lines.sort()
    return lines


# --- clause: main :: () -> None ---
def main():
    lines = droppable(read_input())
    sys.stdout.write("%d\n%s\n" % (len(lines), " ".join(map(str, lines))))


if __name__ == "__main__":
    main()
