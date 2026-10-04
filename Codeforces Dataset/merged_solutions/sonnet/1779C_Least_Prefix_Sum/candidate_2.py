import heapq
import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        m = tokens[pos + 1]
        pos += 2
        cases.append((m, tokens[pos:pos + n]))
        pos += n
    return cases


# --- clause: fewest_flips :: (m: int, a: list[int]) -> int ---
def fewest_flips(m, a):
    n = len(a)
    flips = 0
    heap = []
    running = 0
    for i in range(m - 1, 0, -1):
        item = a[i]
        heapq.heappush(heap, -item)
        running += item
        if running > 0:
            top = -heapq.heappop(heap)
            running -= 2 * top
            heapq.heappush(heap, top)
            flips += 1
    heap = []
    running = 0
    for i in range(m, n):
        item = a[i]
        heapq.heappush(heap, item)
        running += item
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
