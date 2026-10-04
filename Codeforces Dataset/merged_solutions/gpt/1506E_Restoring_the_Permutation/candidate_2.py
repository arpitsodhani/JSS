import sys
from bisect import bisect_left

def restore(n, q):
    # CLAUSE: detect_record_boundaries
    cuts = []
    prev = -1
    for i in range(n):
        if q[i] > prev:
            cuts.append(i)
            prev = q[i]
    is_cut = [False] * n
    for i in cuts:
        is_cut[i] = True

    # CLAUSE: collect_unused_values
    taken = bytearray(n + 1)
    for i in cuts:
        taken[q[i]] = 1
    free = []
    for x in range(1, n + 1):
        if not taken[x]:
            free.append(x)

    # CLAUSE: assign_forced_prefix_maxima
    low = [0] * n
    high = [0] * n
    for i in cuts:
        low[i] = q[i]
        high[i] = q[i]

    # CLAUSE: fill_minimal_gaps
    j = 0
    for i in range(n):
        if low[i] == 0:
            low[i] = free[j]
            j += 1

    # CLAUSE: prepare_gap_buckets
    parent = list(range(n + 1))
    present = [False] * (n + 1)
    for x in free:
        present[x] = True

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for x in range(1, n + 1):
        if not present[x]:
            parent[x] = find(x - 1)

    # CLAUSE: fill_maximal_gaps
    for i in range(n):
        if high[i] == 0:
            v = find(q[i] - 1)
            high[i] = v
            parent[v] = find(v - 1)

    # CLAUSE: emit_restored_permutations
    return low, high

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    at = 1
    ans = []
    for _ in range(t):
        n = nums[at]
        at += 1
        q = nums[at:at + n]
        at += n
        low, high = restore(n, q)
        ans.append(" ".join(str(x) for x in low))
        ans.append(" ".join(str(x) for x in high))
    print("\n".join(ans))

main()
