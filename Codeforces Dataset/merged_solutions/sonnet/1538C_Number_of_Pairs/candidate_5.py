import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        l = raw[reader + 1]
        r = raw[reader + 2]
        reader += 3
        cases.append((l, r, raw[reader:reader + n]))
        reader += n
    return cases


# --- clause: upper_bound :: (a: list[int], value: int) -> int ---
def upper_bound(a, value):
    n = len(a)
    if n == 0 or a[0] > value:
        return 0
    reach = 1
    while reach < n and a[reach] <= value:
        reach *= 2
    low = reach // 2
    high = reach if reach < n else n
    while low + 1 < high:
        mid = (low + high) // 2
        if a[mid] <= value:
            low = mid
        else:
            high = mid
    return low + 1


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
