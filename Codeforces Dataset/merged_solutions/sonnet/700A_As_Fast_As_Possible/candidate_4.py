import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]


# --- clause: fastest_time :: (n: int, l: int, v1: int, v2: int, k: int) -> float ---
def fastest_time(n, l, v1, v2, k):
    groups = (n + k - 1) // k
    low = l / float(v2)
    high = l / float(v1)
    for _ in range(200):
        mid = (low + high) / 2
        ride = v2 * (l - v1 * mid) / float(v2 - v1)
        if ride <= 0:
            high = mid
            continue
        back = ride * (v2 - v1) / (v2 * float(v1 + v2))
        if groups * ride / v2 + (groups - 1) * back <= mid:
            high = mid
        else:
            low = mid
    return high


# --- clause: main :: () -> None ---
def main():
    n, l, v1, v2, k = read_input()
    sys.stdout.write("%.10f\n" % fastest_time(n, l, v1, v2, k))


if __name__ == "__main__":
    main()
