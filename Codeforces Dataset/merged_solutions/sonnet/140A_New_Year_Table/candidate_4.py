import math
import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: plates_fit :: (n: int, big: int, small: int) -> bool ---
def plates_fit(n, big, small):
    if small > big:
        return False
    if n == 1:
        return True
    room = big - small
    if room < small:
        return n == 2 and 2 * small <= big
    span = 2 * math.asin(small / float(room))
    return n * span <= 2 * math.pi + 1e-9


# --- clause: main :: () -> None ---
def main():
    n, big, small = read_input()
    sys.stdout.write("YES\n" if plates_fit(n, big, small) else "NO\n")


if __name__ == "__main__":
    main()
