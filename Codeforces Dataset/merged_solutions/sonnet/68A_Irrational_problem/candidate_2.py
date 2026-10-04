import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[:4], data[4], data[5]


# --- clause: count_fixed :: (mods: list[int], a: int, b: int) -> int ---
def count_fixed(mods, a, b):
    smallest = mods[0]
    for value in mods:
        if value < smallest:
            smallest = value
    total = 0
    for x in range(a, b + 1):
        if x < smallest:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    mods, a, b = read_input()
    sys.stdout.write(str(count_fixed(mods, a, b)) + "\n")


if __name__ == "__main__":
    main()
