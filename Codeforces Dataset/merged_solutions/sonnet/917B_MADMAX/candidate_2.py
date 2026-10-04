import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        edges.append((int(data[idx]), int(data[idx + 1]), data[idx + 2][0] - 97))
        idx += 3
    return n, m, edges


# --- clause: build_adj :: (n: int, edges: list[tuple[int, int, int]]) -> list[list[tuple[int, int]]] ---
def build_adj(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((v, c))
    for u in range(1, n + 1):
        adj[u].sort(key=lambda pair: pair[1])
    return adj


# --- clause: can_win :: (u: int, v: int, c: int, adj: list, memo: dict) -> bool ---
def can_win(u, v, c, adj, memo):
    key = (u, v, c)
    cached = memo.get(key)
    if cached is not None:
        return cached
    answer = False
    for nxt, ch in adj[u]:
        if ch < c:
            continue
        if not can_win(v, nxt, ch, adj, memo):
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
    sys.stdout.write("%s\n" % "\n".join(winner_table(n, build_adj(n, edges))))


if __name__ == "__main__":
    main()
