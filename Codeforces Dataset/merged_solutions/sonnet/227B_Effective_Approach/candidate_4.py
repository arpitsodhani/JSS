import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    a = numbers[1:1 + n]
    m = numbers[1 + n]
    return a, numbers[2 + n:2 + n + m]


# --- clause: count_steps :: (a: list[int], queries: list[int]) -> tuple[int, int] ---
def count_steps(a, queries):
    n = len(a)
    where = [0] * (n + 1)
    for i in range(n):
        where[a[i]] = i + 1
    front = 0
    for value in queries:
        front += where[value]
    back = (n + 1) * len(queries) - front
    return front, back


# --- clause: main :: () -> None ---
def main():
    a, queries = read_input()
    sys.stdout.write("%d %d\n" % count_steps(a, queries))


if __name__ == "__main__":
    main()
