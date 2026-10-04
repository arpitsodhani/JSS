import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2], tokens[3], tokens[4]


# --- clause: fastest_time :: (n: int, l: int, v1: int, v2: int, k: int) -> float ---
def fastest_time(n, l, v1, v2, k):
    groups = (n + k - 1) // k
    ride = l / (1.0 + 2.0 * v1 * (groups - 1) / (v1 + v2))
    return ride / v2 + (l - ride) / v1


# --- clause: main :: () -> None ---
def main():
    n, l, v1, v2, k = read_input()
    sys.stdout.write("%.10f\n" % fastest_time(n, l, v1, v2, k))


if __name__ == "__main__":
    main()
