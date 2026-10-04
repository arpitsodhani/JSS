import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    battles = []
    pos = 2
    for _ in range(m):
        u = int(data[pos])
        pos += 1
        v = int(data[pos])
        pos += 1
        battles.append((u, v))
    return n, m, battles


# --- clause: unique_order :: (n: int, battles: list[tuple[int, int]], k: int) -> bool ---
def unique_order(n, battles, k):
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(k):
        u, v = battles[i]
        adj[u].append(v)
        indeg[v] += 1
    ready = []
    for node in range(n, 0, -1):
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
        mid = (low + high) // 2
        if unique_order(n, battles, mid):
            high = mid
        else:
            low = mid + 1
    return low


# --- clause: main :: () -> None ---
def main():
    n, m, battles = read_input()
    result = find_answer(n, m, battles)
    sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    main()
