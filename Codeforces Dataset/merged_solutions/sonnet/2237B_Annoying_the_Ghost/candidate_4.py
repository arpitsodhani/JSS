import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        a = numbers[cursor:cursor + n]
        cursor += n
        b = numbers[cursor:cursor + n]
        cursor += n
        cases.append((a, b))
    return cases


# --- clause: fewest_swaps :: (a: list[int], b: list[int]) -> int ---
def fewest_swaps(a, b):
    import heapq

    n = len(a)
    waiting = [[] for _ in range(n + 1)]
    for i in range(n):
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if b[mid] >= a[i]:
                high = mid
            else:
                low = mid + 1
        if low >= n:
            return -1
        waiting[low].append(i)
    ready = []
    order = []
    for spot in range(n):
        for i in waiting[spot]:
            heapq.heappush(ready, i)
        if len(ready) == 0:
            return -1
        order.append(heapq.heappop(ready))
    total = 0
    seen = []
    for value in order:
        for other in seen:
            if other > value:
                total += 1
        seen.append(value)
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b in read_input():
        out.append(fewest_swaps(a, b))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
