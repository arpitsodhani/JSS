import heapq
import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        m = numbers[reader + 1]
        reader += 2
        cases.append((m, numbers[reader:reader + n]))
        reader += n
    return cases


# --- clause: fewest_flips :: (m: int, a: list[int]) -> int ---
def fewest_flips(m, a):
    n = len(a)
    flips = 0
    heap = []
    running = 0
    spot = m - 1
    while spot > 0:
        value = a[spot]
        heapq.heappush(heap, -value)
        running += value
        while running > 0:
            top = -heapq.heappop(heap)
            running -= 2 * top
            heapq.heappush(heap, top)
            flips += 1
        spot -= 1
    heap = []
    running = 0
    spot = m
    while spot < n:
        value = a[spot]
        heapq.heappush(heap, value)
        running += value
        while running < 0:
            low = heapq.heappop(heap)
            running -= 2 * low
            heapq.heappush(heap, -low)
            flips += 1
        spot += 1
    return flips


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, a in read_input():
        out.append(fewest_flips(m, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
