import heapq
import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int]], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    islands = []
    offset = 2
    for _ in range(n):
        islands.append((data[offset], data[offset + 1]))
        offset += 2
    gaps = []
    for i in range(n - 1):
        floor_value = islands[i + 1][0] - islands[i][1]
        ceiling_value = islands[i + 1][1] - islands[i][0]
        gaps.append((floor_value, ceiling_value))
    return gaps, data[offset:offset + m]


# --- clause: assign_bridges :: (gaps: list[tuple[int, int]], bridges: list[int]) -> list[int] | None ---
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
        if len(pending) == 0:
            continue
        ceiling_value, index = pending[0]
        if ceiling_value < length:
            return None
        heapq.heappop(pending)
        answer[index] = which + 1
    if pending or seen < len(order):
        return None
    return answer


# --- clause: main :: () -> None ---
def main():
    gaps, bridges = read_input()
    answer = assign_bridges(gaps, bridges)
    if answer is None:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write("Yes\n" + " ".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
