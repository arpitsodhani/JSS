import heapq
import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        m = raw[offset + 1]
        offset += 2
        cases.append((m, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: fewest_flips :: (m: int, a: list[int]) -> int ---
def fewest_flips(m, a):
    n = len(a)
    flips = 0
    heap = []
    running = 0
    for i in range(m - 1, 0, -1):
        number = a[i]
        heapq.heappush(heap, -number)
        running += number
        if running > 0:
            top = -heapq.heappop(heap)
            running -= 2 * top
            heapq.heappush(heap, top)
            flips += 1
    heap = []
    running = 0
    for i in range(m, n):
        number = a[i]
        heapq.heappush(heap, number)
        running += number
        if running < 0:
            low = heapq.heappop(heap)
            running -= 2 * low
            heapq.heappush(heap, -low)
            flips += 1
    return flips


# --- clause: main :: () -> None ---
def main():
    out = []
    for m, a in read_input():
        out.append(fewest_flips(m, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
