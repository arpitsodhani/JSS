import sys

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    q = nums[0]
    cursor = 1
    lines = []

    for _ in range(q):
        n = nums[cursor]
        cursor += 1
        seq = nums[cursor:cursor + n]
        cursor += n

        # CLAUSE: collect_value_spans
        first = {}
        last = {}
        seen_order = []
        for idx, value in enumerate(seq):
            if value not in first:
                first[value] = idx
                seen_order.append(value)
            last[value] = idx

        # CLAUSE: order_distinct_values
        seen_order.sort()

        # CLAUSE: evaluate_adjacent_compatibility
        chain = [0] * len(seen_order)
        for i in range(len(seen_order) - 1):
            a = seen_order[i]
            b = seen_order[i + 1]
            chain[i + 1] = 1 if last[a] < first[b] else 0

        # CLAUSE: extend_kept_value_window
        longest = len(seen_order) > 0
        left = 0
        for right in range(len(seen_order)):
            if right > 0 and chain[right] == 0:
                left = right
            length = right - left + 1
            if length > longest:
                longest = length

        # CLAUSE: compute_minimum_operations
        lines.append(str(len(seen_order) - longest))

        # CLAUSE: reset_per_query_state
        first = None
        last = None
        seen_order = None
        chain = None

    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
