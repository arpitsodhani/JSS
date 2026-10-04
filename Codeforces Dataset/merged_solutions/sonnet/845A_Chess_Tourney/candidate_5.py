import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return n, raw[1:1 + 2 * n]


# --- clause: can_split :: (n: int, ratings: list[int]) -> bool ---
def can_split(n, ratings):
    queue_order = sorted(ratings)
    return queue_order[n - 1] < queue_order[n]


# --- clause: main :: () -> None ---
def main():
    n, ratings = read_input()
    sys.stdout.write("YES\n" if can_split(n, ratings) else "NO\n")


if __name__ == "__main__":
    main()
