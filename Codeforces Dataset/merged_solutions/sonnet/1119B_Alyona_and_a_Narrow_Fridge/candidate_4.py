import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    h = numbers[1]
    return h, numbers[2:2 + n]


# --- clause: fits :: (h: int, a: list[int], k: int) -> bool ---
def fits(h, a, k):
    ranked = sorted(a[:k])
    total = 0
    i = k - 1
    while i >= 0:
        total += ranked[i]
        i -= 2
    return total <= h


# --- clause: most_bottles :: (h: int, a: list[int]) -> int ---
def most_bottles(h, a):
    best = 0
    k = 1
    while k <= len(a):
        if fits(h, a, k):
            best = k
        k += 1
    return best


# --- clause: main :: () -> None ---
def main():
    h, a = read_input()
    sys.stdout.write("%d\n" % most_bottles(h, a))


if __name__ == "__main__":
    main()
