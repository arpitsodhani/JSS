import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: best_arc :: (n: int, a: int) -> int ---
def best_arc(n, a):
    best = 1
    gap = abs(180 - a * n)
    arc = 2
    while arc <= n - 2:
        here = abs(arc * 180 - a * n)
        if here < gap:
            gap = here
            best = arc
        arc += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    arc = best_arc(n, a)
    sys.stdout.write("1 2 %d\n" % (n + 1 - arc))


if __name__ == "__main__":
    main()
