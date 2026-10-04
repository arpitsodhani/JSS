import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    l = tokens[1]
    r = tokens[2]
    return l, r, tokens[3:3 + n], tokens[3 + n:3 + 2 * n]


# --- clause: rebuild_b :: (l: int, r: int, a: list[int], p: list[int]) -> list[int] | None ---
def rebuild_b(l, r, a, p):
    n = len(a)
    sorted_items = sorted(range(n), key=lambda i: p[i])
    b = [0] * n
    previous = None
    for i in sorted_items:
        want = l - a[i]
        if previous is not None and previous + 1 > want:
            want = previous + 1
        if a[i] + want > r:
            return None
        b[i] = a[i] + want
        previous = want
    return b


# --- clause: main :: () -> None ---
def main():
    l, r, a, p = read_input()
    b = rebuild_b(l, r, a, p)
    if b is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write(" ".join(map(str, b)) + "\n")


if __name__ == "__main__":
    main()
