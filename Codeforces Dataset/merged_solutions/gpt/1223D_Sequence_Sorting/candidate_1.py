import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n

        # CLAUSE: collect_value_spans
        first = {}
        last = {}
        for i, x in enumerate(a):
            if x not in first:
                first[x] = i
            last[x] = i

        # CLAUSE: order_distinct_values
        values = sorted(first)

        # CLAUSE: evaluate_adjacent_compatibility
        compatible = []
        for i in range(len(values) - 1):
            left = values[i]
            right = values[i + 1]
            compatible.append(last[left] < first[right])

        # CLAUSE: extend_kept_value_window
        longest = 1 if values else 0
        current = 1 if values else 0
        for ok in compatible:
            if ok:
                current += 1
            else:
                current = 1
            if current > longest:
                longest = current

        # CLAUSE: compute_minimum_operations
        out.append(str(len(values) - longest))

        # CLAUSE: reset_per_query_state
        first.clear()
        last.clear()

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
