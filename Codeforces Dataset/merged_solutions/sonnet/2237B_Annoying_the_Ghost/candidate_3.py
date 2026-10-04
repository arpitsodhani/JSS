import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        a = fields[offset:offset + n]
        offset += n
        b = fields[offset:offset + n]
        offset += n
        cases.append((a, b))
    return cases


# --- clause: fewest_swaps :: (a: list[int], b: list[int]) -> int ---
def fewest_swaps(a, b):
    import bisect
    import heapq

    n = len(a)
    waiting = [[] for _ in range(n + 1)]
    for i in range(n):
        spot = bisect.bisect_left(b, a[i])
        if spot >= n:
            return -1
        waiting[spot].append(i)
    ready = []
    order = []
    for spot in range(n):
        for i in waiting[spot]:
            heapq.heappush(ready, i)
        if not ready:
            return -1
        order.append(heapq.heappop(ready))
    summed = 0
    for i in range(n):
        for j in range(i + 1, n):
            if order[i] > order[j]:
                summed += 1
    return summed


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(fewest_swaps(a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
