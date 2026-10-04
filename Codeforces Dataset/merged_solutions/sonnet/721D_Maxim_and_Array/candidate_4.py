import heapq
import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    x = numbers[2]
    return k, x, numbers[3:3 + n]


# --- clause: count_negatives :: (a: list[int]) -> int ---
def count_negatives(a):
    total = 0
    for entry in a:
        if entry < 0:
            total += 1
    return total


# --- clause: apply_moves :: (k: int, x: int, a: list[int]) -> None ---
def apply_moves(k, x, a):
    negatives = count_negatives(a)
    heap = []
    for i in range(len(a)):
        heapq.heappush(heap, (abs(a[i]), i))
    left = k
    while left:
        size, spot = heapq.heappop(heap)
        if size != abs(a[spot]):
            continue
        want_low = negatives % 2 == 0
        step = x if (a[spot] >= 0) != want_low else -x
        was = a[spot] < 0
        a[spot] += step
        if (a[spot] < 0) != was:
            negatives += 1 if a[spot] < 0 else -1
        heapq.heappush(heap, (abs(a[spot]), spot))
        left -= 1


# --- clause: main :: () -> None ---
def main():
    k, x, a = read_input()
    apply_moves(k, x, a)
    sys.stdout.write(" ".join(map(str, a)) + "\n")


if __name__ == "__main__":
    main()
