import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    rest = ''.join(data[2:])
    
    board = [list(rest[i * m:(i + 1) * m]) for i in range(n)]
    
    whites = {}
    black_id = {}
    black_cells = []
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'w':
                whites[(i, j)] = len(whites)
            elif board[i][j] == 'b':
                black_id[(i, j)] = len(black_cells)
                black_cells.append((i, j))
    
    if len(whites) != 2 * len(black_cells):
        print("NO")
        return
    
    option_cells = []
    black_options = [[] for _ in black_cells]
    
    for bid, (i, j) in enumerate(black_cells):
        for (di, dj) in ((0, 1), (1, 0)):
            a = (i - di, j - dj)
            c = (i + di, j + dj)
            if a in whites and c in whites:
                oid = len(option_cells)
                option_cells.append((bid, whites[a], whites[c]))
                black_options[bid].append(oid)
    
    if any(len(opts) == 0 for opts in black_options):
        print("NO")
        return
    
    b = len(black_cells)
    o = len(option_cells)
    w = len(whites)
    
    source = 0
    black_start = 1
    option_start = black_start + b
    white_start = option_start + o
    sink = white_start + w
    size = sink + 1
    
    graph = [[] for _ in range(size)]
    
    def add_edge(v, u, cap):
        graph[v].append([u, cap, len(graph[u])])
        graph[u].append([v, 0, len(graph[v]) - 1])
    
    for bid in range(b):
        add_edge(source, black_start + bid, 2)
        for oid in black_options[bid]:
            add_edge(black_start + bid, option_start + oid, 2)
    
    for oid, (_, w1, w2) in enumerate(option_cells):
        add_edge(option_start + oid, white_start + w1, 1)
        add_edge(option_start + oid, white_start + w2, 1)
    
    for wid in range(w):
        add_edge(white_start + wid, sink, 1)
    
    flow = 0
    need = 2 * b
    
    while True:
        parent = [None] * size
        q = deque([source])
        parent[source] = (-1, -1)
        
        while q and parent[sink] is None:
            v = q.popleft()
            for ei, edge in enumerate(graph[v]):
                u, cap, _ = edge
                if cap > 0 and parent[u] is None:
                    parent[u] = (v, ei)
                    q.append(u)
                    if u == sink:
                        break
        
        if parent[sink] is None:
            break
        
        add = need - flow
        v = sink
        while v != source:
            p, ei = parent[v]
            add = min(add, graph[p][ei][1])
            v = p
        
        v = sink
        while v != source:
            p, ei = parent[v]
            edge = graph[p][ei]
            rev = edge[2]
            edge[1] -= add
            graph[v][rev][1] += add
            v = p
        
        flow += add
        if flow == need:
            break
    
    if flow != need:
        print("NO")
        return
    
    result = [['.' if board[i][j] == '.' else '?' for j in range(m)] for i in range(n)]
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    used = [False] * b
    
    for bid, (i, j) in enumerate(black_cells):
        chosen = -1
        node = black_start + bid
        for edge in graph[node]:
            u, cap, _ = edge
            if option_start <= u < option_start + o and cap == 0:
                chosen = u - option_start
                break
        
        if chosen == -1:
            print("NO")
            return
        
        obid, w1, w2 = option_cells[chosen]
        if obid != bid or used[bid]:
            print("NO")
            return
        
        used[bid] = True
        ch = letters[bid % len(letters)]
        result[i][j] = ch
        
        cells = []
        for pos, wid in whites.items():
            if wid == w1 or wid == w2:
                cells.append(pos)
        
        for x, y in cells:
            result[x][y] = ch
    
    print("YES")
    print('\n'.join(''.join(row) for row in result))

if __name__ == "__main__":
    main()
