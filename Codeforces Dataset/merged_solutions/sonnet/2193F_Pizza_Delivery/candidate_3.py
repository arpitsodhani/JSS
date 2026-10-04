import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        ax = fields[cursor + 1]
        ay = fields[cursor + 2]
        bx = fields[cursor + 3]
        by = fields[cursor + 4]
        cursor += 5
        xs = fields[cursor:cursor + n]
        cursor += n
        ys = fields[cursor:cursor + n]
        cursor += n
        cases.append((ax, ay, bx, by, xs, ys))
    return cases


# --- clause: column_spans :: (xs: list[int], ys: list[int]) -> list[tuple[int, int]] ---
def column_spans(xs, ys):
    rows = {}
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        if x in rows:
            lower, high = rows[x]
            if y < lower:
                lower = y
            if y > high:
                high = y
            rows[x] = (lower, high)
        else:
            rows[x] = (y, y)
    return [rows[x] for x in sorted(rows)]


# --- clause: walk_time :: (ax: int, ay: int, bx: int, by: int, spans: list[tuple[int, int]]) -> int ---
def walk_time(ax, ay, bx, by, spans):
    huge = 1 << 62
    here = [ay]
    cost = [0]
    for lower, high in spans:
        fresh = [lower, high]
        prices = [huge, huge]
        for i in range(len(here)):
            spot = here[i]
            paid = cost[i]
            reach = paid + abs(spot - high) + (high - lower)
            if reach < prices[0]:
                prices[0] = reach
            reach = paid + abs(spot - lower) + (high - lower)
            if reach < prices[1]:
                prices[1] = reach
        here = fresh
        cost = prices
    best = huge
    for i in range(len(here)):
        total = cost[i] + abs(here[i] - by)
        if total < best:
            best = total
    return best + bx - ax


# --- clause: main :: () -> None ---
def main():
    out = []
    for ax, ay, bx, by, xs, ys in read_input():
        out.append(walk_time(ax, ay, bx, by, column_spans(xs, ys)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
