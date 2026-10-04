import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    battles = []
    idx = 2
    for _ in range(m):
        winner, loser = int(data[idx]), int(data[idx + 1])
        idx += 2
        battles.append((winner, loser))
    return n, m, battles


# --- clause: unique_order :: (n: int, battles: list[tuple[int, int]], k: int) -> bool ---
def unique_order(n, battles, k):
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(k):
        winner, loser = battles[i]
        adj[winner].append(loser)
        indeg[loser] += 1
    ready = []
    for node in range(1, n + 1):
        if not indeg[node]:
            ready.append(node)
    for _ in range(n):
        if len(ready) != 1:
            return False
        node = ready.pop()
        for beaten in adj[node]:
            indeg[beaten] -= 1
            if not indeg[beaten]:
                ready.append(beaten)
    return True


# --- clause: find_answer :: (n: int, m: int, battles: list[tuple[int, int]]) -> int ---
def find_answer(n, m, battles):
    if not unique_order(n, battles, m):
        return -1
    low, high = 1, m
    while low < high:
        mid = low + (high - low) // 2
        if unique_order(n, battles, mid):
            high = mid
        else:
            low = mid + 1
    return high


# --- clause: main :: () -> None ---
def main():
    n, m, battles = read_input()
    sys.stdout.write("%d\n" % find_answer(n, m, battles))


if __name__ == "__main__":
    main()
