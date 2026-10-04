import heapq
import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    x = data[2]
    return k, x, data[3:3 + n]


# --- clause: count_negatives :: (a: list[int]) -> int ---
def count_negatives(a):
    total = 0
    for value in a:
        if value < 0:
            total += 1
    return total


# --- clause: apply_moves :: (k: int, x: int, a: list[int]) -> None ---
def apply_moves(k, x, a):
    negatives = count_negatives(a)
    heap = []
    for i in range(len(a)):
        heap.append((abs(a[i]), i))
    heapq.heapify(heap)
    for _ in range(k):
        while True:
            size, spot = heap[0]
            if size == abs(a[spot]):
                break
            heapq.heappop(heap)
        heapq.heappop(heap)
        was_low = a[spot] < 0
        if negatives % 2 == 0:
            if a[spot] >= 0:
                a[spot] -= x
            else:
                a[spot] += x
        else:
            if a[spot] >= 0:
                a[spot] += x
            else:
                a[spot] -= x
        now_low = a[spot] < 0
        if was_low != now_low:
            negatives += 1 if now_low else -1
        heapq.heappush(heap, (abs(a[spot]), spot))


# --- clause: main :: () -> None ---
def main():
    k, x, a = read_input()
    apply_moves(k, x, a)
    sys.stdout.write(" ".join(map(str, a)) + "\n")


if __name__ == "__main__":
    main()
