import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: fewest_coins :: (a: list[int]) -> int ---
def fewest_coins(a):
    sorted_items = sorted(a, reverse=True)
    total = sum(a)
    mine = 0
    taken = 0
    for value in sorted_items:
        if mine * 2 > total:
            break
        mine += value
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_coins(read_input()))


if __name__ == "__main__":
    main()
