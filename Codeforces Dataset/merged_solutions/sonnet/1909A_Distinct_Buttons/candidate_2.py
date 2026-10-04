import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append([(tokens[at + 2 * i], tokens[at + 2 * i + 1]) for i in range(n)])
        at += 2 * n
    return cases


# --- clause: reachable :: (points: list[tuple[int, int]]) -> bool ---
def reachable(points):
    right = True
    left = True
    up = True
    down = True
    for x, y in points:
        if x < 0:
            right = False
        if x > 0:
            left = False
        if y < 0:
            up = False
        if y > 0:
            down = False
    return right or left or up or down


# --- clause: main :: () -> None ---
def main():
    out = []
    for points in read_input():
        out.append("YES" if reachable(points) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
