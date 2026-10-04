import sys
from heapq import heappush, heappop

INF = 10 ** 30

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        cur_dist, u = heappop(heap)
        if cur_dist != dist[u]:
            continue
        
        for v, w, edge_id in graph[u]:
            new_dist = cur_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                parent[v] = u
                parent_edge[v] = edge_id
                heappush(heap, (new_dist, v))
    
    return dist, parent, parent_edge

def build_components(n, edges, parent_edge, path_nodes, path_pos):
    tree = [[] for _ in range(n + 1)]
    
    for v in range(1, n + 1):
        edge_id = parent_edge[v]
        if edge_id == -1:
            continue
        u, to, _ = edges[edge_id]
        p = u ^ to ^ v
        tree[v].append(p)
        tree[p].append(v)
    
    comp = [-1] * (n + 1)
    
    for i, root in enumerate(path_nodes):
        comp[root] = i
        stack = [root]
        
        while stack:
            u = stack.pop()
            for v in tree[u]:
                edge_id = -1
                if parent_edge[u] != -1:
                    a, b, _ = edges[parent_edge[u]]
                    if (a ^ b ^ u) == v:
                        edge_id = parent_edge[u]
                if edge_id == -1 and parent_edge[v] != -1:
                    a, b, _ = edges[parent_edge[v]]
                    if (a ^ b ^ v) == u:
                        edge_id = parent_edge[v]
                
                if edge_id in path_pos:
                    continue
                
                if comp[v] == -1:
                    comp[v] = i
                    stack.append(v)
    
    return comp

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    q = int(data[idx + 2])
    idx += 3
    
    edges = []
    graph = [[] for _ in range(n + 1)]
    
    for edge_id in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3
        
        edges.append((u, v, w))
        graph[u].append((v, w, edge_id))
        graph[v].append((u, w, edge_id))
    
    dist_start, parent_start, parent_edge_start = dijkstra(1, graph, n)
    dist_end, parent_end, parent_edge_end = dijkstra(n, graph, n)
    
    shortest = dist_start[n]
    
    path_nodes = []
    path_edges = []
    cur = n
    
    while cur != 1:
        path_nodes.append(cur)
        path_edges.append(parent_edge_start[cur])
        cur = parent_start[cur]
    
    path_nodes.append(1)
    path_nodes.reverse()
    path_edges.reverse()
    
    path_pos = {edge_id: i for i, edge_id in enumerate(path_edges)}
    path_len = len(path_edges)
    
    for i, edge_id in enumerate(path_edges):
        parent_end[path_nodes[i]] = path_nodes[i + 1]
        parent_edge_end[path_nodes[i]] = edge_id
    
    comp_start = build_components(n, edges, parent_edge_start, path_nodes, path_pos)
    comp_end = build_components(n, edges, parent_edge_end, path_nodes, path_pos)
    
    size = 1
    while size < path_len:
        size *= 2
    
    seg = [INF] * (2 * size)
    
    def update(l, r, value):
        l += size
        r += size
        
        while l <= r:
            if l % 2 == 1:
                seg[l] = min(seg[l], value)
                l += 1
            if r % 2 == 0:
                seg[r] = min(seg[r], value)
                r -= 1
            l //= 2
            r //= 2
    
    for edge_id, (u, v, w) in enumerate(edges):
        if edge_id in path_pos:
            continue
        
        a = comp_start[u]
        b = comp_end[v]
        if a < b:
            update(a, b - 1, dist_start[u] + w + dist_end[v])
        
        a = comp_start[v]
        b = comp_end[u]
        if a < b:
            update(a, b - 1, dist_start[v] + w + dist_end[u])
    
    best_avoid = [INF] * path_len
    for i in range(path_len):
        pos = i + size
        value = INF
        while pos:
            value = min(value, seg[pos])
            pos //= 2
        best_avoid[i] = value
    
    answers = []
    
    for _ in range(q):
        edge_id = int(data[idx]) - 1
        x = int(data[idx + 1])
        idx += 2
        
        u, v, _ = edges[edge_id]
        
        with_changed = min(
            dist_start[u] + x + dist_end[v],
            dist_start[v] + x + dist_end[u]
        )
        
        if edge_id in path_pos:
            answers.append(str(min(best_avoid[path_pos[edge_id]], with_changed)))
        else:
            answers.append(str(min(shortest, with_changed)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
