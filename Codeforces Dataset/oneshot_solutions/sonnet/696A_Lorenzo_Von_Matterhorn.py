import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    q = int(input_data[idx])
    idx += 1
    
    edge_cost = {}  # edge_cost[node] = cost of edge from node to its parent
    
    def find_lca(u, v):
        # Find ancestors of u
        ancestors_u = set()
        node = u
        while node >= 1:
            ancestors_u.add(node)
            if node == 1:
                break
            node //= 2
        
        # Find first ancestor of v that's also ancestor of u
        node = v
        while node >= 1:
            if node in ancestors_u:
                return node
            if node == 1:
                break
            node //= 2
        
        return 1
    
    def get_edges_on_path(u, v):
        lca = find_lca(u, v)
        edges = []
        
        # Edges from u to lca
        node = u
        while node != lca:
            edges.append(node)
            node //= 2
        
        # Edges from v to lca (will be reversed to get lca to v)
        node = v
        path_from_v = []
        while node != lca:
            path_from_v.append(node)
            node //= 2
        
        # Add reversed path to get full path u -> lca -> v
        edges.extend(reversed(path_from_v))
        
        return edges
    
    for _ in range(q):
        event_type = int(input_data[idx])
        idx += 1
        
        if event_type == 1:
            # Update: increase path from u to v by w
            v = int(input_data[idx])
            idx += 1
            u = int(input_data[idx])
            idx += 1
            w = int(input_data[idx])
            idx += 1
            
            edges = get_edges_on_path(u, v)
            for edge in edges:
                edge_cost[edge] = edge_cost.get(edge, 0) + w
        else:  # event_type == 2
            # Query: cost of path from v to u
            v = int(input_data[idx])
            idx += 1
            u = int(input_data[idx])
            idx += 1
            
            edges = get_edges_on_path(v, u)
            cost = sum(edge_cost.get(edge, 0) for edge in edges)
            print(cost)

if __name__ == "__main__":
    main()
