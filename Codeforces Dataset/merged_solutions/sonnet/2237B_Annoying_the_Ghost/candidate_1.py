import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
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
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if order[i] > order[j]:
                total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(fewest_swaps(a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
