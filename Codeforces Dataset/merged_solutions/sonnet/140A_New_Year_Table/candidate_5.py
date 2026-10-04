import math
import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2]


# --- clause: plates_fit :: (n: int, big: int, small: int) -> bool ---
def plates_fit(n, big, small):
    if small > big:
        return False
    if n == 1:
        return True
    if 2 * small > big:
        return False
    return (big - small) * math.sin(math.pi / n) >= small - 1e-9


# --- clause: main :: () -> None ---
def main():
    n, big, small = read_input()
    sys.stdout.write("YES\n" if plates_fit(n, big, small) else "NO\n")


if __name__ == "__main__":
    main()
