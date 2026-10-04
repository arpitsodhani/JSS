import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: has_triangle :: (n: int, likes: list[int]) -> bool ---
def has_triangle(n, likes):
    for i in range(1, n + 1):
        b = likes[i - 1]
        c = likes[b - 1]
        if c == i:
            continue
        if likes[c - 1] == i:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    n, likes = read_input()
    sys.stdout.write("YES\n" if has_triangle(n, likes) else "NO\n")


if __name__ == "__main__":
    main()
