import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: has_triangle :: (n: int, likes: list[int]) -> bool ---
def has_triangle(n, likes):
    for first in range(1, n + 1):
        second = likes[first - 1]
        if second == first:
            continue
        third = likes[second - 1]
        if third == first or third == second:
            continue
        if likes[third - 1] == first:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    n, likes = read_input()
    sys.stdout.write("YES\n" if has_triangle(n, likes) else "NO\n")


if __name__ == "__main__":
    main()
