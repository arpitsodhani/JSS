import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    pos = 2
    for _ in range(m):
        u = int(data[pos])
        pos += 1
        v = int(data[pos])
        pos += 1
        c = data[pos][0] - 97
        pos += 1
        edges.append((u, v, c))
    return n, m, edges


# --- clause: build_adj :: (n: int, edges: list[tuple[int, int, int]]) -> list[list[tuple[int, int]]] ---
def build_adj(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((v, c))
    return adj


# --- clause: can_win :: (u: int, v: int, c: int, adj: list, memo: dict) -> bool ---
def can_win(u, v, c, adj, memo):
    key = u * 100000 + v * 1000 + c
    if key in memo:
        return memo[key]
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
            if can_win(i, j, 0, adj, memo):
                row.append("A")
            else:
                row.append("B")
        rows.append("".join(row))
    return rows


# --- clause: main :: () -> None ---
def main():
    n, m, edges = read_input()
    print("\n".join(winner_table(n, build_adj(n, edges))))


if __name__ == "__main__":
    main()
