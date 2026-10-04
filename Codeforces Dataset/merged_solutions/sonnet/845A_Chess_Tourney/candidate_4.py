import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return n, numbers[1:1 + 2 * n]


# --- clause: can_split :: (n: int, ratings: list[int]) -> bool ---
def can_split(n, ratings):
    order = sorted(ratings)
    weaker = 0
    for value in order:
        if value < order[n]:
            weaker += 1
    return weaker >= n


# --- clause: main :: () -> None ---
def main():
    n, ratings = read_input()
    sys.stdout.write("YES\n" if can_split(n, ratings) else "NO\n")


if __name__ == "__main__":
    main()
