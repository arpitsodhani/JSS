import sys


# --- clause: read_input :: () -> tuple[int, int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    rows = []
    pos = 2
    for _ in range(n):
        rows.append(data[pos:pos + m])
        pos += m
    return n, m, rows


# --- clause: pair_for :: (n: int, m: int, rows: list[list[int]], limit: int) -> tuple[int, int] | None ---
def pair_for(n, m, rows, limit):
    full = (1 << m) - 1
    owner = {}
    for index in range(n):
        mask = 0
        row = rows[index]
        for bit in range(m):
            if row[bit] >= limit:
                mask |= 1 << bit
        if mask not in owner:
            owner[mask] = index + 1
    for first in owner:
        for second in owner:
            if first | second == full:
                return owner[first], owner[second]
    return None


# --- clause: best_pair :: (n: int, m: int, rows: list[list[int]]) -> tuple[int, int] ---
def best_pair(n, m, rows):
    seen = set()
    for row in rows:
        for value in row:
            seen.add(value)
    values = sorted(seen)
    answer = pair_for(n, m, rows, values[0])
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) >> 1
        found = pair_for(n, m, rows, values[middle])
        if found is None:
            high = middle - 1
        else:
            answer = found
            low = middle + 1
    return answer


# --- clause: main :: () -> None ---
def main():
    n, m, rows = read_input()
    first, second = best_pair(n, m, rows)
    sys.stdout.write("%d %d\n" % (first, second))


if __name__ == "__main__":
    main()
