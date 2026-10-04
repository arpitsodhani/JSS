import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        cases.append((m, data[pos:pos + n]))
        pos += n
    return cases

# Clause fewest_flips [Confidence: 1.00]
def fewest_flips(m, a):
    n = len(a)
    flips = 0
    heap = []
    running = 0
    for i in range(m - 1, 0, -1):
        element = a[i]
        heapq.heappush(heap, -element)
        running += element
        if running > 0:
            top = -heapq.heappop(heap)
            running -= 2 * top
            heapq.heappush(heap, top)
            flips += 1
    heap = []
    running = 0
    for i in range(m, n):
        element = a[i]
        heapq.heappush(heap, element)
        running += element
        if running < 0:
            low = heapq.heappop(heap)
            running -= 2 * low
            heapq.heappush(heap, -low)
            flips += 1
    return flips

# Clause main [Confidence: 1.00]
def main():
    out = []
    for m, a in read_input():
        out.append(fewest_flips(m, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

