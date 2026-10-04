import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        k = data[pos]
        pos += 1
        cases.append(data[pos:pos + k])
        pos += k
    return cases

# Clause fibonacci_blocks [Confidence: 1.00]
def fibonacci_blocks(total):
    blocks = []
    a = 1
    b = 1
    left = total
    while left > 0:
        blocks.append(a)
        left -= a
        a, b = b, a + b
    if left != 0:
        return None
    return blocks

# Clause can_arrange [Confidence: 1.00]
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
        left = -best - size
        if left < 0:
            return False
        if left:
            heapq.heappush(heap, (-left, letter))
        previous = letter
    return True

# Clause main [Confidence: 1.00]
def main():
    out = []
    for counts in read_input():
        out.append("YES" if can_arrange(counts) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

