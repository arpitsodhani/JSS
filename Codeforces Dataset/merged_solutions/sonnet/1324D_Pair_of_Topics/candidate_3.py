import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return fields[1:1 + n], fields[1 + n:1 + 2 * n]


# --- clause: count_good :: (a: list[int], b: list[int]) -> int ---
def count_good(a, b):
    gaps = sorted(a[i] - b[i] for i in range(len(a)))
    total = 0
    start = 0
    finish = len(gaps) - 1
    while start < finish:
        if gaps[start] + gaps[finish] > 0:
            total += finish - start
            finish -= 1
        else:
            start += 1
    return total


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % count_good(a, b))


if __name__ == "__main__":
    main()
