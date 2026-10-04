import sys
import heapq

def build(n, q):
    # CLAUSE: detect_record_boundaries
    new_max = [i == 0 or q[i] != q[i - 1] for i in range(n)]
    starts = []
    for i, flag in enumerate(new_max):
        if flag:
            starts.append((i, q[i]))

    # CLAUSE: collect_unused_values
    fixed_values = {value for _, value in starts}
    leftovers = []
    for value in range(1, n + 1):
        if value not in fixed_values:
            leftovers.append(value)

    # CLAUSE: assign_forced_prefix_maxima
    smallest = [None] * n
    largest = [None] * n
    for i, value in starts:
        smallest[i] = value
        largest[i] = value

    # CLAUSE: fill_minimal_gaps
    fill_iter = iter(leftovers)
    for i in range(n):
        if smallest[i] is None:
            smallest[i] = next(fill_iter)

    # CLAUSE: prepare_gap_buckets
    groups = []
    for k, (left, value) in enumerate(starts):
        right = starts[k + 1][0] if k + 1 < len(starts) else n
        groups.append((left + 1, right, value))
    heaps = {}
    p = 0
    for left, right, value in groups:
        heap = []
        while p < len(leftovers) and leftovers[p] < value:
            heapq.heappush(heap, -leftovers[p])
            p += 1
        heaps[value] = heap

    # CLAUSE: fill_maximal_gaps
    for left, right, value in groups:
        heap = heaps[value]
        for i in range(left, right):
            largest[i] = -heapq.heappop(heap)

    # CLAUSE: emit_restored_permutations
    return smallest, largest

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    index = 1
    lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        q = list(map(int, data[index:index + n]))
        index += n
        a, b = build(n, q)
        lines.append(" ".join(map(str, a)))
        lines.append(" ".join(map(str, b)))
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
