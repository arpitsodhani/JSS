import sys

def restore_one(n, q):
    # CLAUSE: detect_record_boundaries
    first = [False] * n
    first[0] = True
    for i in range(1, n):
        first[i] = q[i] != q[i - 1]

    # CLAUSE: collect_unused_values
    used = [0] * (n + 1)
    for i in range(n):
        if first[i]:
            used[q[i]] = 1
    spare = [v for v in range(1, n + 1) if used[v] == 0]

    # CLAUSE: assign_forced_prefix_maxima
    left_answer = [0] * n
    right_answer = [0] * n
    for i in range(n):
        if first[i]:
            left_answer[i] = q[i]
            right_answer[i] = q[i]

    # CLAUSE: fill_minimal_gaps
    spare_index = 0
    for i in range(n):
        if left_answer[i] == 0:
            left_answer[i] = spare[spare_index]
            spare_index += 1

    # CLAUSE: prepare_gap_buckets
    parent = list(range(n + 1))
    allowed = [0] * (n + 1)
    for v in spare:
        allowed[v] = 1

    def get(v):
        root = v
        while parent[root] != root:
            root = parent[root]
        while parent[v] != v:
            nxt = parent[v]
            parent[v] = root
            v = nxt
        return root

    for v in range(1, n + 1):
        if allowed[v] == 0:
            parent[v] = get(v - 1)

    # CLAUSE: fill_maximal_gaps
    limit = 0
    for i in range(n):
        if first[i]:
            limit = q[i]
        else:
            chosen = get(limit - 1)
            right_answer[i] = chosen
            parent[chosen] = get(chosen - 1)

    # CLAUSE: emit_restored_permutations
    return left_answer, right_answer

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    k = 1
    result = []
    for _ in range(t):
        n = values[k]
        k += 1
        q = values[k:k + n]
        k += n
        a, b = restore_one(n, q)
        result.append(" ".join(map(str, a)))
        result.append(" ".join(map(str, b)))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
