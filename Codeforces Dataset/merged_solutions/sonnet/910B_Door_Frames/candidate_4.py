import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: fewest_bars :: (n: int, a: int, b: int) -> int ---
def fewest_bars(n, a, b):
    sides = [a, a, a, a, b, b]
    stack = [(0, (0, 0, 0, 0, 0, 0))]
    best = 6
    while stack:
        at, used = stack.pop()
        if at == len(sides):
            bars = 0
            for value in used:
                if value:
                    bars += 1
            if bars < best:
                best = bars
            continue
        for slot in range(len(used)):
            if used[slot] + sides[at] <= n:
                nxt = list(used)
                nxt[slot] += sides[at]
                stack.append((at + 1, tuple(nxt)))
    return best


# --- clause: main :: () -> None ---
def main():
    n, a, b = read_input()
    sys.stdout.write("%d\n" % fewest_bars(n, a, b))


if __name__ == "__main__":
    main()
