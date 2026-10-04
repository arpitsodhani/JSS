import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append([(fields[offset + 2 * i], fields[offset + 2 * i + 1]) for i in range(n)])
        offset += 2 * n
    return cases


# --- clause: reachable :: (points: list[tuple[int, int]]) -> bool ---
def reachable(points):
    right = True
    start = True
    up = True
    down = True
    for x, y in points:
        if x < 0:
            right = False
        if x > 0:
            start = False
        if y < 0:
            up = False
        if y > 0:
            down = False
    return right or start or up or down


# --- clause: main :: () -> None ---
def main():
    out = []
    for points in read_input():
        out.append("YES" if reachable(points) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
