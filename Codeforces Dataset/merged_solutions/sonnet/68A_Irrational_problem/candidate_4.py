import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[:4], data[4], data[5]


# --- clause: count_fixed :: (mods: list[int], a: int, b: int) -> int ---
def count_fixed(mods, a, b):
    smallest = min(mods)
    count = 0
    x = a
    while x <= b and x < smallest:
        count += 1
        x += 1
    return count


# --- clause: main :: () -> None ---
def main():
    mods, a, b = read_input()
    sys.stdout.write(str(count_fixed(mods, a, b)) + "\n")


if __name__ == "__main__":
    main()
