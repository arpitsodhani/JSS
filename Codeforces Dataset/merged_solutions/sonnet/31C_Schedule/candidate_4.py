import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return [(numbers[1 + 2 * i], numbers[2 + 2 * i]) for i in range(n)]


# --- clause: find_clash :: (groups: list[tuple[int, int]], skip: int) -> tuple[int, int] ---
def find_clash(groups, skip):
    ranked = []
    for i in range(len(groups)):
        if i != skip:
            ranked.append((groups[i][0], groups[i][1], i))
    ranked.sort()
    for j in range(1, len(ranked)):
        if ranked[j][0] < ranked[j - 1][1]:
            return ranked[j - 1][2], ranked[j][2]
    return -1, -1


# --- clause: droppable :: (groups: list[tuple[int, int]]) -> list[int] ---
def droppable(groups):
    first, second = find_clash(groups, -1)
    if first < 0:
        return list(range(1, len(groups) + 1))
    out = []
    if find_clash(groups, first)[0] < 0:
        out.append(first + 1)
    if find_clash(groups, second)[0] < 0:
        out.append(second + 1)
    return sorted(out)


# --- clause: main :: () -> None ---
def main():
    out = droppable(read_input())
    sys.stdout.write("%d\n%s\n" % (len(out), " ".join(map(str, out))))


if __name__ == "__main__":
    main()
