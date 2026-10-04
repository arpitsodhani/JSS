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
    if right - left <= 1:
        return -1, -1
    if left == 0 and right == n + 1:
        return 1, n + 1
    if left == 0:
        return 1, right - 1
    if right == n + 1:
        return n, n - left
    return (left + right) // 2, (right - left) // 2


# --- clause: run_records :: (n: int, records: list[tuple[int, int]]) -> list[int] ---
def run_records(n, records):
    after = [0] * (n + 2)
    before = [0] * (n + 2)
    busy = [False] * (n + 2)
    after[0] = n + 1
    before[n + 1] = 0
    busy[0] = True
    busy[n + 1] = True
    spot = {}
    heap = []
    place, reach = gap_choice(n, 0, n + 1)
    heappush(heap, (-reach, place, 0, n + 1))
    out = []
    for kind, car in records:
        if kind == 1:
            place = -1
            left = 0
            right = n + 1
            while heap:
                item = heappop(heap)
                if busy[item[2]] and busy[item[3]] and after[item[2]] == item[3]:
                    place = item[1]
                    left = item[2]
                    right = item[3]
                    break
            out.append(place)
            spot[car] = place
            busy[place] = True
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
            busy[place] = False
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
