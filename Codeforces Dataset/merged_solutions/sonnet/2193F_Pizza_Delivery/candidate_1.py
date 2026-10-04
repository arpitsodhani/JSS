import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        ax = data[pos + 1]
        ay = data[pos + 2]
        bx = data[pos + 3]
        by = data[pos + 4]
        pos += 5
        xs = data[pos:pos + n]
        pos += n
        ys = data[pos:pos + n]
        pos += n
        cases.append((ax, ay, bx, by, xs, ys))
    return cases


# --- clause: column_spans :: (xs: list[int], ys: list[int]) -> list[tuple[int, int]] ---
def column_spans(xs, ys):
    rows = {}
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        if x in rows:
            low, high = rows[x]
            if y < low:
                low = y
            if y > high:
                high = y
            rows[x] = (low, high)
        else:
            rows[x] = (y, y)
    return [rows[x] for x in sorted(rows)]


# --- clause: walk_time :: (ax: int, ay: int, bx: int, by: int, spans: list[tuple[int, int]]) -> int ---
def walk_time(ax, ay, bx, by, spans):
    huge = 1 << 62
    here = [ay]
    cost = [0]
    for low, high in spans:
        fresh = [low, high]
        prices = [huge, huge]
        for i in range(len(here)):
            spot = here[i]
            paid = cost[i]
            reach = paid + abs(spot - high) + (high - low)
            if reach < prices[0]:
                prices[0] = reach
            reach = paid + abs(spot - low) + (high - low)
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
