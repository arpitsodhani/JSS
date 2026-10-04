import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append([(numbers[cursor + 2 * i], numbers[cursor + 2 * i + 1]) for i in range(n)])
        cursor += 2 * n
    return cases


# --- clause: reachable :: (points: list[tuple[int, int]]) -> bool ---
def reachable(points):
    xs = [x for x, y in points]
    ys = [y for x, y in points]
    if min(xs) >= 0 or max(xs) <= 0:
        return True
    return min(ys) >= 0 or max(ys) <= 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for points in read_input():
        out.append("YES" if reachable(points) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
