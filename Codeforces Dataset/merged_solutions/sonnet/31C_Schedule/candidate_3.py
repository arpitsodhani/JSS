import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return [(fields[1 + 2 * i], fields[2 + 2 * i]) for i in range(n)]


# --- clause: find_clash :: (groups: list[tuple[int, int]], skip: int) -> tuple[int, int] ---
def find_clash(groups, skip):
    arranged = []
    for i in range(len(groups)):
        if i != skip:
            arranged.append((groups[i][0], groups[i][1], i))
    arranged.sort()
    for j in range(1, len(arranged)):
        if arranged[j][0] < arranged[j - 1][1]:
            return arranged[j - 1][2], arranged[j][2]
    return -1, -1


# --- clause: droppable :: (groups: list[tuple[int, int]]) -> list[int] ---
def droppable(groups):
    a, b = find_clash(groups, -1)
    if a < 0:
        return [i + 1 for i in range(len(groups))]
    pieces = []
    for skip in (a, b):
        if find_clash(groups, skip)[0] < 0:
            pieces.append(skip + 1)
    pieces.sort()
    return pieces


# --- clause: main :: () -> None ---
def main():
    pieces = droppable(read_input())
    sys.stdout.write("%d\n%s\n" % (len(pieces), " ".join(map(str, pieces))))


if __name__ == "__main__":
    main()
