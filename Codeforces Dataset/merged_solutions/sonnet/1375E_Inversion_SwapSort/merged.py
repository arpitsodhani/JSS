# Clause setup_environment [Confidence: 0.60]
import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]


# Clause solve_logic [Confidence: 0.60]
    pairs = [(values[i], i) for i in range(n)]
    pairs.sort()

    rank_at_index = [0] * n
    index_at_rank = [0] * n
    for rank, item in enumerate(pairs):
        idx = item[1]
        rank_at_index[idx] = rank
        index_at_rank[rank] = idx

    pending = []
    for rank in range(n - 2, -1, -1):
        if index_at_rank[rank] > index_at_rank[rank + 1]:
            pending.append(rank)

    swaps = []

    def add_if_needed(rank):
        if 0 <= rank < n - 1 and index_at_rank[rank] > index_at_rank[rank + 1]:
            pending.append(rank)

    while pending:
        rank = pending.pop()
        if not (0 <= rank < n - 1):
            continue
        first = index_at_rank[rank]
        second = index_at_rank[rank + 1]
        if first < second:
            continue

        low = second + 1
        high = first + 1
        swaps.append((low, high))

        rank_at_index[first], rank_at_index[second] = rank_at_index[second], rank_at_index[first]
        index_at_rank[rank], index_at_rank[rank + 1] = second, first

        add_if_needed(rank - 1)
        add_if_needed(rank)
        add_if_needed(rank + 1)


# Clause finish_program [Confidence: 0.60]
    output = [str(len(operations))]
    output.extend(f"{left} {right}" for left, right in operations)
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()


