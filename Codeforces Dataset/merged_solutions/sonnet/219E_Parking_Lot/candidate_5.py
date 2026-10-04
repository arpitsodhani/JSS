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
    after = [0] * (n + 2)
    before = [0] * (n + 2)
    taken = [False] * (n + 2)
    after[0] = n + 1
    before[n + 1] = 0
    spot = {}
    heap = []
    place, reach = gap_choice(n, 0, n + 1)
    heappush(heap, (-reach, place, 0, n + 1))
    out = []
    for kind, car in records:
        if kind == 1:
            while True:
                neg, place, left, right = heappop(heap)
                if left and not taken[left]:
                    continue
                if right <= n and not taken[right]:
                    continue
                if after[left] == right:
                    break
            out.append(place)
            spot[car] = place
            taken[place] = True
            after[left] = place
            before[place] = left
            after[place] = right
            before[right] = place
            for lo, hi in ((left, place), (place, right)):
                pos, reach = gap_choice(n, lo, hi)
                if pos > 0:
                    heappush(heap, (-reach, pos, lo, hi))
        else:
            place = spot.pop(car)
            taken[place] = False
            left = before[place]
            right = after[place]
            after[left] = right
            before[right] = left
            pos, reach = gap_choice(n, left, right)
            if pos > 0:
                heappush(heap, (-reach, pos, left, right))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, records = read_input()
    sys.stdout.write("\n".join(map(str, run_records(n, records))) + "\n")


if __name__ == "__main__":
    main()
