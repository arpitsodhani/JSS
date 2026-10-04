# CLAUSE: setup_environment
import sys
import heapq

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n, k, b, c = nums[:4]
    values = nums[4:4 + n]
    block = min(b, 5 * c)
    best = 10 ** 30

# CLAUSE: solve_logic
    for residue in range(5):
        events = []
        for value in values:
            quotient, rem = divmod(value, 5)
            if residue >= rem:
                start = quotient
                fixed = (residue - rem) * c - quotient * block
            else:
                start = quotient + 1
                fixed = (residue - rem + 5) * c - (quotient + 1) * block
            events.append((start, fixed))

        events.sort()
        heap = []
        total = 0
        idx = 0

        while idx < n:
            current = events[idx][0]
            while idx < n and events[idx][0] == current:
                val = events[idx][1]
                if len(heap) < k:
                    heapq.heappush(heap, -val)
                    total += val
                elif val < -heap[0]:
                    total += val + heapq.heappop(heap)
                    heapq.heappush(heap, -val)
                idx += 1
            if len(heap) == k:
                best = min(best, k * current * block + total)

# CLAUSE: finish_program
    print(best)

if __name__ == "__main__":
    main()
