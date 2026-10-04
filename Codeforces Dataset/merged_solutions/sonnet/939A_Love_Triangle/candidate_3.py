import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: has_triangle :: (n: int, likes: list[int]) -> bool ---
def has_triangle(n, likes):
    liked = [0] + likes
    return any(liked[liked[liked[i]]] == i and liked[i] != i and liked[liked[i]] != i
               for i in range(1, n + 1))


# --- clause: main :: () -> None ---
def main():
    n, likes = read_input()
    sys.stdout.write("YES\n" if has_triangle(n, likes) else "NO\n")


if __name__ == "__main__":
    main()
