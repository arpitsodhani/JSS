import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]


# --- clause: find_clash :: (groups: list[tuple[int, int]], skip: int) -> tuple[int, int] ---
def find_clash(groups, skip):
    order = []
    for i in range(len(groups)):
        if i != skip:
            order.append((groups[i][0], groups[i][1], i))
    order.sort()
    for j in range(1, len(order)):
        if order[j][0] < order[j - 1][1]:
            return order[j - 1][2], order[j][2]
    return -1, -1


# --- clause: droppable :: (groups: list[tuple[int, int]]) -> list[int] ---
def droppable(groups):
    a, b = find_clash(groups, -1)
    if a < 0:
        return [i + 1 for i in range(len(groups))]
    out = []
    for skip in (a, b):
        if find_clash(groups, skip)[0] < 0:
            out.append(skip + 1)
    out.sort()
    return out


# --- clause: main :: () -> None ---
def main():
    out = droppable(read_input())
    sys.stdout.write("%d\n%s\n" % (len(out), " ".join(map(str, out))))


if __name__ == "__main__":
    main()
