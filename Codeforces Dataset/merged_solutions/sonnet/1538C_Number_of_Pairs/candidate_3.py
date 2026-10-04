import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        l = fields[offset + 1]
        r = fields[offset + 2]
        offset += 3
        cases.append((l, r, fields[offset:offset + n]))
        offset += n
    return cases


# --- clause: upper_bound :: (a: list[int], value: int) -> int ---
def upper_bound(a, value):
    small = 0
    high = len(a)
    while small < high:
        mid = (small + high) // 2
        if a[mid] <= value:
            small = mid + 1
        else:
            high = mid
    return small


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
