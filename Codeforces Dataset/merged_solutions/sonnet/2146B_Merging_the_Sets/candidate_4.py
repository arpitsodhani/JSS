import sys


# --- clause: read_input :: () -> list[tuple[int, list[list[int]]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        reader += 2
        sets = []
        for _ in range(n):
            size = numbers[reader]
            reader += 1
            sets.append(numbers[reader:reader + size])
            reader += size
        cases.append((m, sets))
    return cases


# --- clause: has_three_ways :: (m: int, sets: list[list[int]]) -> bool ---
def has_three_ways(m, sets):
    cover = {}
    for group in sets:
        for value in group:
            cover[value] = cover.get(value, 0) + 1
    if len(cover) < m:
        return False
    spare = 0
    for group in sets:
        extra = True
        i = 0
        while i < len(group):
            if cover[group[i]] < 2:
                extra = False
                break
            i += 1
        if extra:
            spare += 1
    return spare >= 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, sets in read_input():
        out.append("YES" if has_three_ways(m, sets) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
