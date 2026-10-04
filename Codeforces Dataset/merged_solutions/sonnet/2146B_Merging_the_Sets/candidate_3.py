import sys


# --- clause: read_input :: () -> list[tuple[int, list[list[int]]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        m = fields[cursor + 1]
        cursor += 2
        sets = []
        for _ in range(n):
            extent = fields[cursor]
            cursor += 1
            sets.append(fields[cursor:cursor + extent])
            cursor += extent
        cases.append((m, sets))
    return cases


# --- clause: has_three_ways :: (m: int, sets: list[list[int]]) -> bool ---
def has_three_ways(m, sets):
    cover = [0] * (m + 1)
    for group in sets:
        for value in group:
            cover[value] += 1
    for value in range(1, m + 1):
        if cover[value] == 0:
            return False
    spare = 0
    for group in sets:
        loose = True
        for value in group:
            if cover[value] < 2:
                loose = False
                break
        if loose:
            spare += 1
        if spare >= 2:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, sets in read_input():
        out.append("YES" if has_three_ways(m, sets) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
