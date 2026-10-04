import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    l = numbers[1]
    r = numbers[2]
    return l, r, numbers[3:3 + n], numbers[3 + n:3 + 2 * n]


# --- clause: could_be_true :: (l: int, r: int, a: list[int], b: list[int]) -> bool ---
def could_be_true(l, r, a, b):
    if a[:l - 1] != b[:l - 1]:
        return False
    if a[r:] != b[r:]:
        return False
    tally = {}
    for value in a[l - 1:r]:
        tally[value] = tally.get(value, 0) + 1
    for value in b[l - 1:r]:
        if tally.get(value, 0) == 0:
            return False
        tally[value] -= 1
    return True


# --- clause: main :: () -> None ---
def main():
    l, r, a, b = read_input()
    sys.stdout.write("TRUTH\n" if could_be_true(l, r, a, b) else "LIE\n")


if __name__ == "__main__":
    main()
