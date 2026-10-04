import sys
import heapq

def make_answers(n, q):
    # CLAUSE: detect_record_boundaries
    boundary = [0] * n
    record_values = []
    current = 0
    for i in range(n):
        if q[i] != current:
            boundary[i] = 1
            current = q[i]
            record_values.append(current)

    # CLAUSE: collect_unused_values
    occupied = [False] * (n + 1)
    for value in record_values:
        occupied[value] = True
    rest = []
    for value in range(1, n + 1):
        if not occupied[value]:
            rest.append(value)

    # CLAUSE: assign_forced_prefix_maxima
    ans_min = [0] * n
    ans_max = [0] * n
    for i in range(n):
        if boundary[i]:
            ans_min[i] = q[i]
            ans_max[i] = q[i]

    # CLAUSE: fill_minimal_gaps
    need = 0
    for i in range(n):
        if boundary[i] == 0:
            ans_min[i] = rest[need]
            need += 1

    # CLAUSE: prepare_gap_buckets
    waiting = [[] for _ in range(n + 1)]
    record_set = set(record_values)
    target = 0
    for value in range(1, n + 1):
        if value in record_set:
            target = value
        elif target:
            waiting[target].append(-value)
    for value in record_values:
        heapq.heapify(waiting[value])

    # CLAUSE: fill_maximal_gaps
    active = 0
    for i in range(n):
        if boundary[i]:
            active = q[i]
        else:
            ans_max[i] = -heapq.heappop(waiting[active])

    # CLAUSE: emit_restored_permutations
    return ans_min, ans_max

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    output = []
    for _ in range(t):
        n = next(it)
        q = [next(it) for _ in range(n)]
        x, y = make_answers(n, q)
        output.append(" ".join(map(str, x)))
        output.append(" ".join(map(str, y)))
    sys.stdout.write("\n".join(output))

main()
