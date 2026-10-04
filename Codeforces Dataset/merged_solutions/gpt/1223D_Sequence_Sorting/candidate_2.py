import sys

def solve_case(arr):
    # CLAUSE: collect_value_spans
    spans = {}
    for idx in range(len(arr)):
        value = arr[idx]
        if value in spans:
            spans[value][1] = idx
        else:
            spans[value] = [idx, idx]

    # CLAUSE: order_distinct_values
    ordered = sorted(spans.items())

    # CLAUSE: evaluate_adjacent_compatibility
    breaks = [False] * max(0, len(ordered) - 1)
    for i in range(1, len(ordered)):
        prev_value, prev_span = ordered[i - 1]
        cur_value, cur_span = ordered[i]
        breaks[i - 1] = prev_span[1] < cur_span[0]

    # CLAUSE: extend_kept_value_window
    best = 0
    run = 0
    for i in range(len(ordered)):
        if i == 0 or breaks[i - 1]:
            run += 1
        else:
            run = 1
        best = max(best, run)

    # CLAUSE: compute_minimum_operations
    answer = len(ordered) - best

    # CLAUSE: reset_per_query_state
    spans = {}
    ordered = []
    breaks = []

    return answer

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    q = tokens[0]
    at = 1
    ans = []
    for _ in range(q):
        n = tokens[at]
        at += 1
        ans.append(str(solve_case(tokens[at:at + n])))
        at += n
    print("\n".join(ans))

if __name__ == "__main__":
    main()
