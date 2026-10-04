import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return n, tokens[1:1 + 2 * n]


# --- clause: can_split :: (n: int, ratings: list[int]) -> bool ---
def can_split(n, ratings):
    sorted_items = sorted(ratings)
    return sorted_items[n - 1] < sorted_items[n]


# --- clause: main :: () -> None ---
def main():
    n, ratings = read_input()
    sys.stdout.write("YES\n" if can_split(n, ratings) else "NO\n")


if __name__ == "__main__":
    main()
