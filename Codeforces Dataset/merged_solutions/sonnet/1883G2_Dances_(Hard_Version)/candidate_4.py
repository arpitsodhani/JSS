import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        reader += 2
        a = numbers[reader:reader + n - 1]
        reader += n - 1
        b = numbers[reader:reader + n]
        reader += n
        cases.append((m, a, b))
    return cases


# --- clause: removals_for :: (first: int, a: list[int], b: list[int]) -> int ---
def removals_for(first, a, b):
    left = a + [first]
    left.sort()
    n = len(left)
    matched = 0
    i = 0
    for value in b:
        if i < n and left[i] < value:
            matched += 1
            i += 1
    return n - matched


# --- clause: total_removals :: (m: int, a: list[int], b: list[int]) -> int ---
def total_removals(m, a, b):
    a = sorted(a)
    b = sorted(b)
    cheap = removals_for(1, a, b)
    dear = removals_for(m, a, b)
    if cheap == dear:
        return m * cheap
    low = 1
    high = m
    while low + 1 < high:
        mid = (low + high) // 2
        if removals_for(mid, a, b) == cheap:
            low = mid
        else:
            high = mid
    return low * cheap + (m - low) * dear


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, a, b in read_input():
        out.append(total_removals(m, a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
