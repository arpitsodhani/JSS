import sys
import heapq

def solve_case(n, q):
    # CLAUSE: detect_record_boundaries
    record = [False] * n
    last = 0
    for i, x in enumerate(q):
        if x != last:
            record[i] = True
            last = x

    # CLAUSE: collect_unused_values
    used = [False] * (n + 1)
    for i, x in enumerate(q):
        if record[i]:
            used[x] = True
    unused = [x for x in range(1, n + 1) if not used[x]]

    # CLAUSE: assign_forced_prefix_maxima
    mn = [0] * n
    mx = [0] * n
    for i, x in enumerate(q):
        if record[i]:
            mn[i] = x
            mx[i] = x

    # CLAUSE: fill_minimal_gaps
    ptr = 0
    for i in range(n):
        if not record[i]:
            mn[i] = unused[ptr]
            ptr += 1

    # CLAUSE: prepare_gap_buckets
    buckets = [[] for _ in range(n + 1)]
    records = sorted(q[i] for i in range(n) if record[i])
    r = 0
    for v in unused:
        while r + 1 < len(records) and records[r] < v:
            r += 1
        buckets[records[r]].append(-v)
    for h in buckets:
        if h:
            heapq.heapify(h)

    # CLAUSE: fill_maximal_gaps
    active = 0
    for i, x in enumerate(q):
        if record[i]:
            active = x
        else:
            mx[i] = -heapq.heappop(buckets[active])

    # CLAUSE: emit_restored_permutations
    return " ".join(map(str, mn)), " ".join(map(str, mx))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        q = data[pos:pos + n]
        pos += n
        a, b = solve_case(n, q)
        out.append(a)
        out.append(b)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
