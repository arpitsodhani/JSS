import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    l = tokens[1]
    r = tokens[2]
    return l, r, tokens[3:3 + n], tokens[3 + n:3 + 2 * n]


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
