import heapq
import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        k = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + k])
        offset += k
    return cases


# --- clause: fibonacci_blocks :: (total: int) -> list[int] | None ---
def fibonacci_blocks(total):
    blocks = []
    a = 1
    b = 1
    start = total
    while start > 0:
        blocks.append(a)
        start -= a
        a, b = b, a + b
    if start != 0:
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
        start = -best - size
        if start < 0:
            return False
        if start:
            heapq.heappush(heap, (-start, letter))
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
