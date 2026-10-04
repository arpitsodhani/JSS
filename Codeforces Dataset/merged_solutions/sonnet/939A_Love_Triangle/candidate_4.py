import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: has_triangle :: (n: int, likes: list[int]) -> bool ---
def has_triangle(n, likes):
    found = False
    index = 1
    while index <= n and not found:
        b = likes[index - 1]
        c = likes[b - 1]
        if c != index and likes[c - 1] == index:
            found = True
        index += 1
    return found


# --- clause: main :: () -> None ---
def main():
    n, likes = read_input()
    sys.stdout.write("YES\n" if has_triangle(n, likes) else "NO\n")


if __name__ == "__main__":
    main()
