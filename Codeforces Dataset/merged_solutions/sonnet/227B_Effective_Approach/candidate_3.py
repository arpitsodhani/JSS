import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    a = fields[1:1 + n]
    m = fields[1 + n]
    return a, fields[2 + n:2 + n + m]


# --- clause: count_steps :: (a: list[int], queries: list[int]) -> tuple[int, int] ---
def count_steps(a, queries):
    n = len(a)
    where = {}
    for i in range(n):
        where[a[i]] = i + 1
    front = 0
    back = 0
    for element in queries:
        spot = where[element]
        front += spot
        back += n - spot + 1
    return front, back


# --- clause: main :: () -> None ---
def main():
    a, queries = read_input()
    sys.stdout.write("%d %d\n" % count_steps(a, queries))


if __name__ == "__main__":
    main()
