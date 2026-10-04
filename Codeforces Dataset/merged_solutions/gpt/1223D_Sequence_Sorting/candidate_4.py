import sys

def answer_for(a):
    # CLAUSE: collect_value_spans
    position = {}
    for i, x in enumerate(a):
        pair = position.get(x)
        if pair is None:
            position[x] = [i, i]
        else:
            pair[1] = i

    # CLAUSE: order_distinct_values
    ordered_values = sorted(position.keys())
    intervals = [position[x] for x in ordered_values]

    # CLAUSE: evaluate_adjacent_compatibility
    ok = [True]
    for i in range(len(intervals) - 1):
        ok.append(intervals[i][1] < intervals[i + 1][0])

    # CLAUSE: extend_kept_value_window
    dp = [0] * len(intervals)
    longest = 0
    for i in range(len(intervals)):
        if i == 0 or not ok[i]:
            dp[i] = 1
        else:
            dp[i] = dp[i - 1] + 1
        longest = max(longest, dp[i])

    # CLAUSE: compute_minimum_operations
    res = len(intervals) - longest

    # CLAUSE: reset_per_query_state
    position.clear()
    intervals.clear()
    dp.clear()

    return res

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    index = 1
    output = []
    for _ in range(q):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        output.append(str(answer_for(arr)))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
