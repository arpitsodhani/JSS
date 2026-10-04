import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        l = numbers[cursor + 1]
        r = numbers[cursor + 2]
        cursor += 3
        cases.append((l, r, numbers[cursor:cursor + n]))
        cursor += n
    return cases


# --- clause: upper_bound :: (a: list[int], value: int) -> int ---
def upper_bound(a, value):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= value:
            low = mid + 1
        else:
            high = mid
    return low


# --- clause: count_pairs :: (l: int, r: int, a: list[int]) -> int ---
def count_pairs(l, r, a):
    a = sorted(a)
    total = 0
    for value in a:
        total += upper_bound(a, r - value) - upper_bound(a, l - value - 1)
        if l <= 2 * value <= r:
            total -= 1
    return total // 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for l, r, a in read_input():
        out.append(count_pairs(l, r, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
