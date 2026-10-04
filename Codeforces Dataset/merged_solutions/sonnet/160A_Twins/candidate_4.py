import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: fewest_coins :: (a: list[int]) -> int ---
def fewest_coins(a):
    order = sorted(a)
    theirs = sum(a)
    mine = 0
    taken = 0
    while mine <= theirs:
        value = order.pop()
        mine += value
        theirs -= value
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_coins(read_input()))


if __name__ == "__main__":
    main()
