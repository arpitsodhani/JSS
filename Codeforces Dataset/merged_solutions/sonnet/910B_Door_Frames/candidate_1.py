import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2]


# --- clause: fewest_bars :: (n: int, a: int, b: int) -> int ---
def fewest_bars(n, a, b):
    sides = [a, a, a, a, b, b]
    best = 6
    for mask in range(6 ** 6):
        code = mask
        used = [0] * 6
        for i in range(6):
            used[code % 6] += sides[i]
            code //= 6
        if max(used) > n:
            continue
        bars = 0
        for value in used:
            if value:
                bars += 1
        if bars < best:
            best = bars
    return best


# --- clause: main :: () -> None ---
def main():
    n, a, b = read_input()
    sys.stdout.write("%d\n" % fewest_bars(n, a, b))


if __name__ == "__main__":
    main()
