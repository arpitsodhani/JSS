import sys
from heapq import heappush, heappop


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    records = []
    pos = 2
    for _ in range(m):
        records.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, records


# --- clause: gap_choice :: (n: int, left: int, right: int) -> tuple[int, int] ---
def gap_choice(n, left, right):
    free = right - left - 1
    if free <= 0:
        return -1, -1
    if left == 0:
        if right == n + 1:
            return 1, n + 1
        return 1, right - 1
    if right == n + 1:
        return n, n - left
    middle = left + (right - left) // 2
    return middle, middle - left


# --- clause: run_records :: (n: int, records: list[tuple[int, int]]) -> list[int] ---
def run_records(n, records):
    nxt = [0] * (n + 2)
    prv = [0] * (n + 2)
    live = [False] * (n + 2)
    nxt[0] = n + 1
    prv[n + 1] = 0
    where = {}
    start, reach = gap_choice(n, 0, n + 1)
    heap = [(-reach, start, 0, n + 1)]
    answers = []
    for kind, car in records:
        if kind == 2:
            here = where.pop(car)
            live[here] = False
            left = prv[here]
            right = nxt[here]
            nxt[left] = right
            prv[right] = left
            spot, reach = gap_choice(n, left, right)
            if spot > 0:
                heappush(heap, (-reach, spot, left, right))
            continue
        spot = 0
        while heap:
            neg, spot, left, right = heappop(heap)
            if left and not live[left]:
                continue
            if right <= n and not live[right]:
                continue
            if nxt[left] == right:
                break
        answers.append(spot)
        where[car] = spot
        live[spot] = True
        nxt[left] = spot
        prv[spot] = left
        nxt[spot] = right
        prv[right] = spot
        first, reach = gap_choice(n, left, spot)
        if first > 0:
            heappush(heap, (-reach, first, left, spot))
        second, reach = gap_choice(n, spot, right)
        if second > 0:
            heappush(heap, (-reach, second, spot, right))
    return answers


# --- clause: main :: () -> None ---
def main():
    n, m, records = read_input()
    sys.stdout.write("\n".join(map(str, run_records(n, records))) + "\n")


if __name__ == "__main__":
    main()
