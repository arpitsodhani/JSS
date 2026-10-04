import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: trick_chance :: (n: int, m: int) -> float ---
def trick_chance(n, m):
    if n * m == 1:
        return 1.0
    total = n * m
    same = (total - m) / float(total - 1)
    return (1.0 + (1.0 - same) * (n - 1)) / n


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    sys.stdout.write("%.12f\n" % trick_chance(n, m))


if __name__ == "__main__":
    main()
