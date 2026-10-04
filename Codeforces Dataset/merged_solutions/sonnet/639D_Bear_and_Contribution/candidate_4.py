# CLAUSE: setup_environment
import sys
import heapq

def add_smallest(heap, total, value, limit):
    if len(heap) < limit:
        heapq.heappush(heap, -value)
        return total + value
    if value < -heap[0]:
        removed = heapq.heapreplace(heap, -value)
        return total + value + removed
    return total

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    k = int(raw[1])
    b = int(raw[2])
    c = int(raw[3])
    values = [int(x) for x in raw[4:4 + n]]
    five_cost = b if b < 5 * c else 5 * c
    answer = 10 ** 30

# CLAUSE: solve_logic
    prepared = [[] for _ in range(5)]
    for value in values:
        q, rem = divmod(value, 5)
        for residue in range(rem, 5):
            prepared[residue].append((q, (residue - rem) * c - q * five_cost))
        for residue in range(rem):
            prepared[residue].append((q + 1, (residue - rem + 5) * c - (q + 1) * five_cost))

    for events in prepared:
        events.sort(key=lambda item: item[0])
        chosen = []
        total = 0
        pos = 0
        length = len(events)
        while pos < length:
            q = events[pos][0]
            while pos < length and events[pos][0] == q:
                total = add_smallest(chosen, total, events[pos][1], k)
                pos += 1
            if len(chosen) == k:
                candidate = k * q * five_cost + total
                if candidate < answer:
                    answer = candidate

# CLAUSE: finish_program
    sys.stdout.write(str(answer))

if __name__ == "__main__":
    main()
