import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        ax = raw[offset + 1]
        ay = raw[offset + 2]
        bx = raw[offset + 3]
        by = raw[offset + 4]
        offset += 5
        xs = raw[offset:offset + n]
        offset += n
        ys = raw[offset:offset + n]
        offset += n
        cases.append((ax, ay, bx, by, xs, ys))
    return cases


# --- clause: column_spans :: (xs: list[int], ys: list[int]) -> list[tuple[int, int]] ---
def column_spans(xs, ys):
    rows = {}
    for i in range(0, len(xs)):
        x = xs[i]
        y = ys[i]
        if x in rows:
            floor_value, high = rows[x]
            if y < floor_value:
                floor_value = y
            if y > high:
                high = y
            rows[x] = (floor_value, high)
        else:
            rows[x] = (y, y)
    return [rows[x] for x in sorted(rows)]


# --- clause: walk_time :: (ax: int, ay: int, bx: int, by: int, spans: list[tuple[int, int]]) -> int ---
def walk_time(ax, ay, bx, by, spans):
    huge = 1 << 62
    here = [ay]
    cost = [0]
    for floor_value, high in spans:
        fresh = [floor_value, high]
        prices = [huge, huge]
        for i in range(0, len(here)):
            spot = here[i]
            paid = cost[i]
            reach = paid + abs(spot - high) + (high - floor_value)
            if reach < prices[0]:
                prices[0] = reach
            reach = paid + abs(spot - floor_value) + (high - floor_value)
            if reach < prices[1]:
                prices[1] = reach
        here = fresh
        cost = prices
    best = huge
    for i in range(0, len(here)):
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
