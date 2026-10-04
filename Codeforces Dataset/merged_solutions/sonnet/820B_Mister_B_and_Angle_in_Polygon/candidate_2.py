import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: best_arc :: (n: int, a: int) -> int ---
def best_arc(n, a):
    guess = a * n // 180
    best = 1
    gap = -1
    for arc in (guess - 1, guess, guess + 1, 1, n - 2):
        if arc < 1 or arc > n - 2:
            continue
        here = abs(arc * 180 - a * n)
        if gap < 0 or here < gap:
            gap = here
            best = arc
    return best


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    arc = best_arc(n, a)
    sys.stdout.write("1 2 %d\n" % (n + 1 - arc))


if __name__ == "__main__":
    main()
