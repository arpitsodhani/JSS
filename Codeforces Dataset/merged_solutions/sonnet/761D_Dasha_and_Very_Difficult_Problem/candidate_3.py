import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    l = fields[1]
    r = fields[2]
    return l, r, fields[3:3 + n], fields[3 + n:3 + 2 * n]


# --- clause: rebuild_b :: (l: int, r: int, a: list[int], p: list[int]) -> list[int] | None ---
def rebuild_b(l, r, a, p):
    n = len(a)
    arranged = sorted(range(n), key=lambda i: p[i])
    b = [0] * n
    previous = None
    for i in arranged:
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
