import sys


# --- clause: read_input :: () -> list[list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        pieces = []
        for _ in range(n - 1):
            extent = fields[cursor]
            cursor += 1
            pieces.append(fields[cursor:cursor + extent])
            cursor += extent
        cases.append(pieces)
    return cases


# --- clause: try_start :: (n: int, pieces: list[list[int]], first: int) -> list[int] | None ---
def try_start(n, pieces, first):
    holders = [[] for _ in range(n + 1)]
    for index in range(len(pieces)):
        for value in pieces[index]:
            holders[value].append(index)
    left = [len(piece) for piece in pieces]
    used = [False] * len(pieces)
    placed = [False] * (n + 1)
    order = [first]
    placed[first] = True
    for index in holders[first]:
        left[index] -= 1
    while len(order) < n:
        pick = -1
        for index in range(len(pieces)):
            if not used[index] and left[index] == 1:
                pick = index
                break
        if pick < 0:
            return None
        value = 0
        for candidate in pieces[pick]:
            if not placed[candidate]:
                value = candidate
                break
        if value == 0:
            return None
        used[pick] = True
        placed[value] = True
        order.append(value)
        for index in holders[value]:
            left[index] -= 1
    return order


# --- clause: fits :: (n: int, pieces: list[list[int]], order: list[int]) -> bool ---
def fits(n, pieces, order):
    spot = [0] * (n + 1)
    for i in range(n):
        spot[order[i]] = i
    ends = set()
    for piece in pieces:
        low = n
        high = -1
        for value in piece:
            if spot[value] < low:
                low = spot[value]
            if spot[value] > high:
                high = spot[value]
        if high - low + 1 != len(piece) or high in ends or high == 0:
            return False
        ends.add(high)
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for pieces in read_input():
        n = len(pieces) + 1
        answer = None
        seeds = []
        for piece in pieces:
            if len(piece) == 2:
                seeds.append(piece[0])
                seeds.append(piece[1])
        for first in seeds:
            order = try_start(n, pieces, first)
            if order is not None and fits(n, pieces, order):
                answer = order
                break
        out.append(" ".join(map(str, answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
