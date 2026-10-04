import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: min_height :: (order: list[int]) -> int ---
def min_height(order):
    n = len(order)
    groups = []
    index = 1
    while index < n:
        start = index
        index += 1
        while index < n and order[index] > order[index - 1]:
            index += 1
        groups.append(index - start)
    height = 0
    available = 1
    position = 0
    while position < len(groups):
        taken = 0
        used = 0
        while used < available and position < len(groups):
            taken += groups[position]
            position += 1
            used += 1
        available = taken
        height += 1
    return height


# --- clause: main :: () -> None ---
def main():
    out = []
    for order in read_input():
        out.append(str(min_height(order)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
