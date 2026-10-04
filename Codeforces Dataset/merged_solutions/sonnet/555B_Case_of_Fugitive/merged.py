import heapq
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    islands = []
    cursor = 2
    for _ in range(n):
        islands.append((data[cursor], data[cursor + 1]))
        cursor += 2
    gaps = []
    for i in range(n - 1):
        lower = islands[i + 1][0] - islands[i][1]
        upper = islands[i + 1][1] - islands[i][0]
        gaps.append((lower, upper))
    return gaps, data[cursor:cursor + m]

# Clause assign_bridges [Confidence: 1.00]
def assign_bridges(gaps, bridges):
    order = sorted(range(len(gaps)), key=lambda i: gaps[i][0])
    ranked = sorted(range(len(bridges)), key=lambda i: bridges[i])
    answer = [0] * len(gaps)
    pending = []
    seen = 0
    for which in ranked:
        length = bridges[which]
        while seen < len(order) and gaps[order[seen]][0] <= length:
            index = order[seen]
            heapq.heappush(pending, (gaps[index][1], index))
            seen += 1
        if not pending:
            continue
        high, index = pending[0]
        if high < length:
            return None
        heapq.heappop(pending)
        answer[index] = which + 1
    if pending or seen < len(order):
        return None
    return answer

# Clause main [Confidence: 1.00]
def main():
    gaps, bridges = read_input()
    answer = assign_bridges(gaps, bridges)
    if answer is None:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write("Yes\n" + " ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()

