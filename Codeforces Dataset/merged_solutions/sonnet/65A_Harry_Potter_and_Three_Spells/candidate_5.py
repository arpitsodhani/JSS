import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    return list(map(int, sys.stdin.buffer.read().split()[:6]))


# --- clause: ron_is_right :: (a: int, b: int, c: int, d: int, e: int, f: int) -> bool ---
def ron_is_right(a, b, c, d, e, f):
    if d > 0 and c == 0:
        return True
    if d > 0 and b > 0 and a == 0 and c > 0:
        return True
    if d > 0 and b > 0 and f > 0 and e == 0:
        return True
    if a * c * e == 0:
        return False
    return b * d * f > a * c * e


# --- clause: main :: () -> None ---
def main():
    a, b, c, d, e, f = read_input()
    sys.stdout.write("Ron\n" if ron_is_right(a, b, c, d, e, f) else "Hermione\n")


if __name__ == "__main__":
    main()
