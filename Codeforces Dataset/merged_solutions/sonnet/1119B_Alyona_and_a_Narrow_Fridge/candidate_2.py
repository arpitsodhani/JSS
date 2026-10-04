import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    h = tokens[1]
    return h, tokens[2:2 + n]


# --- clause: fits :: (h: int, a: list[int], k: int) -> bool ---
def fits(h, a, k):
    sorted_items = sorted(a[:k])
    total = 0
    i = k - 1
    while i >= 0:
        total += sorted_items[i]
        i -= 2
    return total <= h


# --- clause: most_bottles :: (h: int, a: list[int]) -> int ---
def most_bottles(h, a):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high + 1) // 2
        if fits(h, a, mid):
            low = mid
        else:
            high = mid - 1
    return low


# --- clause: main :: () -> None ---
def main():
    h, a = read_input()
    sys.stdout.write("%d\n" % most_bottles(h, a))


if __name__ == "__main__":
    main()
