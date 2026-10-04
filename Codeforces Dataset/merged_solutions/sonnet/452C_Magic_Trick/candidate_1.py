import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: trick_chance :: (n: int, m: int) -> float ---
def trick_chance(n, m):
    if n * m == 1:
        return 1.0
    extra = (n - 1) * (m - 1) / float(n * m - 1)
    return (1.0 + extra) / n


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write("%.12f\n" % trick_chance(n, m))


if __name__ == "__main__":
    main()
