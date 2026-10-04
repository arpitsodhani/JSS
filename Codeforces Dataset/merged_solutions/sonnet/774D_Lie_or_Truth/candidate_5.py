import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    l = raw[1]
    r = raw[2]
    return l, r, raw[3:3 + n], raw[3 + n:3 + 2 * n]


# --- clause: could_be_true :: (l: int, r: int, a: list[int], b: list[int]) -> bool ---
def could_be_true(l, r, a, b):
    n = len(a)
    for i in range(n):
        if i < l - 1 or i > r - 1:
            if a[i] != b[i]:
                return False
    return sorted(a[l - 1:r]) == sorted(b[l - 1:r])


# --- clause: main :: () -> None ---
def main():
    l, r, a, b = read_input()
    sys.stdout.write("TRUTH\n" if could_be_true(l, r, a, b) else "LIE\n")


if __name__ == "__main__":
    main()
