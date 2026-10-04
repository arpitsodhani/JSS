import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: best_arc :: (n: int, a: int) -> int ---
def best_arc(n, a):
    low = 1
    high = n - 2
    best = low
    gap = abs(low * 180 - a * n)
    for arc in range(low, high + 1):
        distance = abs(arc * 180 - a * n)
        if distance < gap:
            gap = distance
            best = arc
    return best


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    arc = best_arc(n, a)
    sys.stdout.write("1 2 %d\n" % (n + 1 - arc))


if __name__ == "__main__":
    main()
