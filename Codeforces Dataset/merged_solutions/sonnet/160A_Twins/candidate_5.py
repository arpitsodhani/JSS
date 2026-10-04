import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: fewest_coins :: (a: list[int]) -> int ---
def fewest_coins(a):
    queue_order = sorted(a, reverse=True)
    total = sum(a)
    mine = 0
    taken = 0
    for item in queue_order:
        if mine * 2 > total:
            break
        mine += item
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_coins(read_input()))


if __name__ == "__main__":
    main()
