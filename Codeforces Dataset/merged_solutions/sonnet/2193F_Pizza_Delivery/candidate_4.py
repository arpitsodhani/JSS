import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int, list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        ax = numbers[reader + 1]
        ay = numbers[reader + 2]
        bx = numbers[reader + 3]
        by = numbers[reader + 4]
        reader += 5
        xs = numbers[reader:reader + n]
        reader += n
        ys = numbers[reader:reader + n]
        reader += n
        cases.append((ax, ay, bx, by, xs, ys))
    return cases


# --- clause: column_spans :: (xs: list[int], ys: list[int]) -> list[tuple[int, int]] ---
def column_spans(xs, ys):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    spans = []
    current = -1
    for i in order:
        if xs[i] != current:
            current = xs[i]
            spans.append([ys[i], ys[i]])
        else:
            if ys[i] < spans[-1][0]:
                spans[-1][0] = ys[i]
            if ys[i] > spans[-1][1]:
                spans[-1][1] = ys[i]
    return [(low, high) for low, high in spans]


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
