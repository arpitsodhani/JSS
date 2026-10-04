import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: day_counts :: (a: list[int]) -> list[tuple[int, int]] ---
def day_counts(a):
    order = sorted(a)
    rows = []
    for value in order:
        if rows and rows[-1][0] == value:
            rows[-1][1] += 1
        else:
            rows.append([value, 1])
    return [(day, times) for day, times in rows]


# --- clause: longest_streak :: (rows: list[tuple[int, int]]) -> int ---
def longest_streak(rows):
    best = 0
    plain = 0
    pushed = 0
    previous = -10
    for day, times in rows:
        if day - previous == 1:
            fresh_plain = plain + 1
            if pushed > fresh_plain:
                fresh_plain = pushed
            fresh_pushed = 1
            if pushed > 0 and pushed + 1 > fresh_pushed:
                fresh_pushed = pushed + 1
            if times >= 2 and fresh_plain + 1 > fresh_pushed:
                fresh_pushed = fresh_plain + 1
        elif day - previous == 2 and pushed > 0:
            fresh_plain = pushed + 1
            fresh_pushed = 1
            if times >= 2 and fresh_plain + 1 > fresh_pushed:
                fresh_pushed = fresh_plain + 1
        else:
            fresh_plain = 1
            fresh_pushed = 2 if times >= 2 else 1
        plain = fresh_plain
        pushed = fresh_pushed
        previous = day
        if plain > best:
            best = plain
        if pushed > best:
            best = pushed
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(longest_streak(day_counts(a)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
