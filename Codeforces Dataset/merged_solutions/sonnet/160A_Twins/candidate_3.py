import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: fewest_coins :: (a: list[int]) -> int ---
def fewest_coins(a):
    arranged = sorted(a, reverse=True)
    total = sum(a)
    mine = 0
    taken = 0
    for entry in arranged:
        if mine * 2 > total:
            break
        mine += entry
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % fewest_coins(read_input()))


if __name__ == "__main__":
    main()
