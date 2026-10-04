import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    arcs = []
    for i in range(m):
        arcs.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, m, arcs


# --- clause: augment :: (n: int, adj: list[list[int]], match_left: list[int], match_right: list[int], banned: int) -> bool ---
def augment(n, adj, match_left, match_right, banned):
    parent = [0] * (n + 1)
    seen = [False] * (n + 1)
    queue = [u for u in range(1, n + 1) if u != banned and match_left[u] == 0 and adj[u]]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for w in adj[u]:
            if w == banned or seen[w]:
                continue
            seen[w] = True
            parent[w] = u
            nxt = match_right[w]
            if nxt == 0:
                while w:
                    holder = parent[w]
                    freed = match_left[holder]
                    match_left[holder] = w
                    match_right[w] = holder
                    w = freed
                return True
            queue.append(nxt)
    return False


# --- clause: full_matching :: (n: int, adj: list[list[int]]) -> tuple[int, list[int], list[int]] ---
def full_matching(n, adj):
    match_left = [0] * (n + 1)
    match_right = [0] * (n + 1)
    size = 0
    while augment(n, adj, match_left, match_right, 0):
        size += 1
    return size, match_left, match_right


# --- clause: best_center_score :: (n: int, adj: list[list[int]], incident: list[int]) -> int ---
def best_center_score(n, adj, incident):
    total, base_left, base_right = full_matching(n, adj)
    best = 0
    for v in range(1, n + 1):
        match_left = base_left[:]
        match_right = base_right[:]
        size = total
        if match_left[v]:
            match_right[match_left[v]] = 0
            match_left[v] = 0
            size -= 1
        if match_right[v]:
            match_left[match_right[v]] = 0
            match_right[v] = 0
            size -= 1
        while size < total and augment(n, adj, match_left, match_right, v):
            size += 1
        score = incident[v] + size
        if score > best:
            best = score
    return best


# --- clause: solve :: (n: int, m: int, arcs: list[tuple[int, int]]) -> int ---
def solve(n, m, arcs):
    adj = [[] for _ in range(n + 1)]
    incident = [0] * (n + 1)
    for a, b in arcs:
        adj[a].append(b)
        incident[a] += 1
        if b != a:
            incident[b] += 1
    return 3 * n - 2 + m - 2 * best_center_score(n, adj, incident)


# --- clause: main :: () -> None ---
def main():
    n, m, arcs = read_input()
    sys.stdout.write(str(solve(n, m, arcs)) + "\n")


if __name__ == "__main__":
    main()
