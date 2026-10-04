import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    pos = 2
    for _ in range(m):
        u = int(data[pos])
        v = int(data[pos + 1])
        c = data[pos + 2][0] - 97
        pos += 3
        edges.append((u, v, c))
    return n, m, edges

# Clause build_adj [Confidence: 1.00]
def build_adj(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v, c in edges:
        adj[u].append((v, c))
    return adj

# Clause can_win [Confidence: 0.80]
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

# Clause winner_table [Confidence: 1.00]
def winner_table(n, adj):
    memo = {}
    rows = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append("A" if can_win(i, j, 0, adj, memo) else "B")
        rows.append("".join(row))
    return rows

# Clause main [Confidence: 1.00]
def main():
    n, m, edges = read_input()
    sys.stdout.write("\n".join(winner_table(n, build_adj(n, edges))) + "\n")


if __name__ == "__main__":
    main()

