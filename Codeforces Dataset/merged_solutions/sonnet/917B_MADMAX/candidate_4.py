import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    pos = 2
    while len(edges) < m:
        u = int(data[pos])
        v = int(data[pos + 1])
        c = data[pos + 2][0] - 97
        pos += 3
        edges.append((u, v, c))
    return n, m, edges


# --- clause: build_adj :: (n: int, edges: list[tuple[int, int, int]]) -> list[list[tuple[int, int]]] ---
def build_adj(n, edges):
    adj = []
    for _ in range(n + 1):
        adj.append([])
    for edge in edges:
        adj[edge[0]].append((edge[1], edge[2]))
    return adj


# --- clause: can_win :: (u: int, v: int, c: int, adj: list, memo: dict) -> bool ---
def can_win(u, v, c, adj, memo):
    key = (u, v, c)
    cached = memo.get(key)
    if cached is not None:
        return cached
    answer = False
    for nxt, ch in adj[u]:
        if ch >= c and not can_win(v, nxt, ch, adj, memo):
            answer = True
            break
    memo[key] = answer
    return answer


# --- clause: winner_table :: (n: int, adj: list) -> list[str] ---
def winner_table(n, adj):
    memo = {}
    rows = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append("A" if can_win(i, j, 0, adj, memo) else "B")
        rows.append("".join(row))
    return rows


# --- clause: main :: () -> None ---
def main():
    n, m, edges = read_input()
    adj = build_adj(n, edges)
    rows = winner_table(n, adj)
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
