import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        a = numbers[cursor:cursor + n]
        cursor += n
        b = numbers[cursor:cursor + n]
        cursor += n
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
    seen = [False] * n
    moves = []
    for start in range(n):
        if seen[start] or order[start] == start:
            seen[start] = True
            continue
        cycle = []
        node = start
        while not seen[node]:
            seen[node] = True
            cycle.append(node)
            node = order[node]
        for i in range(len(cycle) - 1, 0, -1):
            moves.append((cycle[0] + 1, cycle[i] + 1))
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
