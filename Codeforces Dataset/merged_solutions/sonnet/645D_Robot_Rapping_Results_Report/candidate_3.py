import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    battles = []
    for i in range(m):
        u = int(data[2 + 2 * i])
        v = int(data[3 + 2 * i])
        battles.append((u, v))
    return n, m, battles


# --- clause: unique_order :: (n: int, battles: list[tuple[int, int]], k: int) -> bool ---
def unique_order(n, battles, k):
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for pair in battles[:k]:
        adj[pair[0]].append(pair[1])
        indeg[pair[1]] += 1
    ready = []
    for node in range(1, n + 1):
        if indeg[node] == 0:
            ready.append(node)
    for _ in range(n):
        if len(ready) != 1:
            return False
        node = ready.pop()
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                ready.append(nxt)
    return True


# --- clause: find_answer :: (n: int, m: int, battles: list[tuple[int, int]]) -> int ---
def find_answer(n, m, battles):
    if not unique_order(n, battles, m):
        return -1
    low = 1
    high = m
    while low < high:
        mid = (low + high) >> 1
        if unique_order(n, battles, mid):
            high = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    n, m, battles = read_input()
    print(find_answer(n, m, battles))


if __name__ == "__main__":
    main()
