import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        m = raw[offset + 1]
        offset += 2
        a = raw[offset:offset + n - 1]
        offset += n - 1
        b = raw[offset:offset + n]
        offset += n
        cases.append((m, a, b))
    return cases


# --- clause: removals_for :: (first: int, a: list[int], b: list[int]) -> int ---
def removals_for(first, a, b):
    begin = a + [first]
    begin.sort()
    n = len(begin)
    matched = 0
    i = 0
    for value in b:
        if i < n and begin[i] < value:
            matched += 1
            i += 1
    return n - matched


# --- clause: total_removals :: (m: int, a: list[int], b: list[int]) -> int ---
def total_removals(m, a, b):
    a = sorted(a)
    b = sorted(b)
    low_cost = removals_for(1, a, b)
    high_cost = removals_for(m, a, b)
    if low_cost == high_cost:
        return m * low_cost
    low = 1
    high = m
    while low < high:
        mid = (low + high) // 2
        if removals_for(mid, a, b) > low_cost:
            high = mid
        else:
            low = mid + 1
    return (low - 1) * low_cost + (m - low + 1) * high_cost


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, a, b in read_input():
        out.append(total_removals(m, a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
