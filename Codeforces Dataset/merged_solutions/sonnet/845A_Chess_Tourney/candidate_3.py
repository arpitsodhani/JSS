import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return n, fields[1:1 + 2 * n]


# --- clause: can_split :: (n: int, ratings: list[int]) -> bool ---
def can_split(n, ratings):
    arranged = sorted(ratings)
    return arranged[n - 1] < arranged[n]


# --- clause: main :: () -> None ---
def main():
    n, ratings = read_input()
    sys.stdout.write("YES\n" if can_split(n, ratings) else "NO\n")


if __name__ == "__main__":
    main()
