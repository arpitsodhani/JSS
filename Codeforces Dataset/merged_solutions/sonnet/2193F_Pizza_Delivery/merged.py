import sys

# Clause read_input [Confidence: 1.00]
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

# Clause column_spans [Confidence: 0.80]
def column_spans(xs, ys):
    rows = {}
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        if x in rows:
            bottom, high = rows[x]
            if y < bottom:
                bottom = y
            if y > high:
                high = y
            rows[x] = (bottom, high)
        else:
            rows[x] = (y, y)
    return [rows[x] for x in sorted(rows)]

# Clause walk_time [Confidence: 1.00]
def walk_time(ax, ay, bx, by, spans):
    huge = 1 << 62
    here = [ay]
    cost = [0]
    for bottom, high in spans:
        fresh = [bottom, high]
        prices = [huge, huge]
        for i in range(len(here)):
            spot = here[i]
            paid = cost[i]
            reach = paid + abs(spot - high) + (high - bottom)
            if reach < prices[0]:
                prices[0] = reach
            reach = paid + abs(spot - bottom) + (high - bottom)
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

# Clause main [Confidence: 1.00]
def main():
    out = []
    for ax, ay, bx, by, xs, ys in read_input():
        out.append(walk_time(ax, ay, bx, by, column_spans(xs, ys)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

