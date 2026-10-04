import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))
    return cases


# --- clause: target_order :: (a: list[int], b: list[int]) -> list[int] | None ---
def target_order(a, b):
    n = len(a)
    where = {}
    for i in range(n):
        where[a[i]] = i
    middle = -1
    couples = []
    taken = [False] * n
    for i in range(n):
        if taken[i]:
            continue
        if a[i] == b[i]:
            if middle >= 0:
                return None
            middle = i
            taken[i] = True
            continue
        j = where.get(b[i], -1)
        if j < 0 or taken[j] or b[j] != a[i]:
            return None
        taken[i] = True
        taken[j] = True
        couples.append((i, j))
    if (middle >= 0) != (n % 2 == 1):
        return None
    order = [0] * n
    left = 0
    for i, j in couples:
        order[left] = i
        order[n - 1 - left] = j
        left += 1
    if middle >= 0:
        order[n // 2] = middle
    return order


# --- clause: swap_moves :: (order: list[int]) -> list[tuple[int, int]] ---
def swap_moves(order):
    n = len(order)
    spot = [0] * n
    now = list(range(n))
    for i in range(n):
        spot[i] = i
    moves = []
    for i in range(n):
        want = order[i]
        j = spot[want]
        if j == i:
            continue
        moves.append((i + 1, j + 1))
        here = now[i]
        now[i], now[j] = now[j], now[i]
        spot[want] = i
        spot[here] = j
    return moves


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        order = target_order(a, b)
        if order is None:
            out.append("-1")
            continue
        moves = swap_moves(order)
        out.append(str(len(moves)))
        for x, y in moves:
            out.append("%d %d" % (x, y))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
