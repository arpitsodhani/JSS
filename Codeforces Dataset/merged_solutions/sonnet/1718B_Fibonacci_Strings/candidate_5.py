import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        k = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + k])
        reader += k
    return cases


# --- clause: fibonacci_blocks :: (total: int) -> list[int] | None ---
def fibonacci_blocks(total):
    blocks = []
    a = 1
    b = 1
    low = total
    while low > 0:
        blocks.append(a)
        low -= a
        a, b = b, a + b
    if low != 0:
        return None
    return blocks


# --- clause: can_arrange :: (counts: list[int]) -> bool ---
def can_arrange(counts):
    blocks = fibonacci_blocks(sum(counts))
    if blocks is None:
        return False
    heap = [(-counts[i], i) for i in range(len(counts))]
    heapq.heapify(heap)
    previous = -1
    for size in reversed(blocks):
        if not heap:
            return False
        best, letter = heapq.heappop(heap)
        if letter == previous:
            if not heap:
                return False
            spare = heapq.heappop(heap)
            heapq.heappush(heap, (best, letter))
            best, letter = spare
        low = -best - size
        if low < 0:
            return False
        if low:
            heapq.heappush(heap, (-low, letter))
        previous = letter
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for counts in read_input():
        out.append("YES" if can_arrange(counts) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
