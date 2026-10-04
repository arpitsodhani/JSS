import sys

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    q = next(it)
    results = []

    for _ in range(q):
        n = next(it)
        arr = [next(it) for _ in range(n)]

        # CLAUSE: collect_value_spans
        first_pos = {}
        last_pos = {}
        for pos, val in enumerate(arr):
            first_pos.setdefault(val, pos)
            last_pos[val] = pos

        # CLAUSE: order_distinct_values
        keys = list(first_pos.keys())
        keys.sort()

        # CLAUSE: evaluate_adjacent_compatibility
        good_edge = {}
        for left, right in zip(keys, keys[1:]):
            good_edge[right] = last_pos[left] < first_pos[right]

        # CLAUSE: extend_kept_value_window
        keep = 0
        best_keep = 0
        previous = None
        for val in keys:
            if previous is None or good_edge[val]:
                keep += 1
            else:
                keep = 1
            if keep > best_keep:
                best_keep = keep
            previous = val

        # CLAUSE: compute_minimum_operations
        results.append(str(len(keys) - best_keep))

        # CLAUSE: reset_per_query_state
        first_pos.clear()
        last_pos.clear()
        good_edge.clear()

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
