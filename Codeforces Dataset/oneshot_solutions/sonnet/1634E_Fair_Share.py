import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

def main():
    tokens = sys.stdin.read().split()
    idx = 0
    
    m = int(tokens[idx])
    idx += 1
    
    arrays = []
    value_to_arrays = defaultdict(list)
    total_count = defaultdict(int)
    
    for i in range(m):
        n = int(tokens[idx])
        idx += 1
        arr = []
        for j in range(n):
            arr.append(int(tokens[idx]))
            idx += 1
        arrays.append(arr)
        
        count_in_array = defaultdict(int)
        for v in arr:
            count_in_array[v] += 1
            total_count[v] += 1
        
        for v, cnt in count_in_array.items():
            value_to_arrays[v].append((i, cnt))
    
    # Check even counts
    for v, cnt in total_count.items():
        if cnt % 2 != 0:
            print("NO")
            return
    
    # Build flow network
    values = sorted(total_count.keys())
    value_to_id = {v: i for i, v in enumerate(values)}
    
    source = 0
    sink = m + len(values) + 1
    num_nodes = sink + 1
    
    graph = [[] for _ in range(num_nodes)]
    
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev
    
    def add_edge(u, v, cap):
        graph[u].append(Edge(v, cap, len(graph[v])))
        graph[v].append(Edge(u, 0, len(graph[u]) - 1))
    
    # Source to arrays
    for i in range(m):
        array_node = i + 1
        cap = len(arrays[i]) // 2
        add_edge(source, array_node, cap)
    
    # Track edges from arrays to values
    array_to_value_edge_idx = {}
    
    # Arrays to values
    for v in values:
        value_node = m + 1 + value_to_id[v]
        for arr_idx, cnt in value_to_arrays[v]:
            array_node = arr_idx + 1
            edge_idx = len(graph[array_node])
            add_edge(array_node, value_node, cnt)
            array_to_value_edge_idx[(arr_idx, v)] = (array_node, edge_idx)
    
    # Values to sink
    for v in values:
        value_node = m + 1 + value_to_id[v]
        add_edge(value_node, sink, total_count[v] // 2)
    
    # Dinic's algorithm
    def bfs():
        level = [-1] * num_nodes
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for edge in graph[u]:
                if edge.cap > 0 and level[edge.to] < 0:
                    level[edge.to] = level[u] + 1
                    queue.append(edge.to)
        return level
    
    def dfs(u, pushed, level, iter_list):
        if u == sink:
            return pushed
        
        while iter_list[u] < len(graph[u]):
            edge = graph[u][iter_list[u]]
            if level[edge.to] == level[u] + 1 and edge.cap > 0:
                tr = dfs(edge.to, min(pushed, edge.cap), level, iter_list)
                if tr > 0:
                    edge.cap -= tr
                    graph[edge.to][edge.rev].cap += tr
                    return tr
            iter_list[u] += 1
        return 0
    
    total_flow = 0
    while True:
        level = bfs()
        if level[sink] < 0:
            break
        iter_list = [0] * num_nodes
        while True:
            f = dfs(source, float('inf'), level, iter_list)
            if f == 0:
                break
            total_flow += f
    
    required_flow = sum(len(arr) // 2 for arr in arrays)
    if total_flow != required_flow:
        print("NO")
        return
    
    # Reconstruct solution
    print("YES")
    for i in range(m):
        # Count how many of each value should go to L
        to_L = defaultdict(int)
        
        count_in_array = defaultdict(int)
        for v in arrays[i]:
            count_in_array[v] += 1
        
        for v, original_cnt in count_in_array.items():
            if (i, v) in array_to_value_edge_idx:
                array_node, edge_idx = array_to_value_edge_idx[(i, v)]
                remaining_cap = graph[array_node][edge_idx].cap
                flow_amount = original_cnt - remaining_cap
                to_L[v] = flow_amount
        
        result = []
        for val in arrays[i]:
            if to_L[val] > 0:
                result.append('L')
                to_L[val] -= 1
            else:
                result.append('R')
        
        print(''.join(result))

main()
