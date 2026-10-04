from collections import deque, defaultdict

def solve():
    n, m = map(int, input().split())
    
    adj = defaultdict(list)
    for _ in range(m):
        u, v, c = map(int, input().split())
        adj[u].append((v, c))
        adj[v].append((u, c))
    
    s, t = map(int, input().split())
    
    if s == t:
        return 0
    
    dist = {}
    dq = deque()
    visited = set()
    
    # Initialize: from s, take any first edge (costs 1 line)
    for neighbor, color in adj[s]:
        state = (neighbor, color)
        dist[state] = 1
        dq.append(state)
    
    while dq:
        state = dq.popleft()
        
        if state in visited:
            continue
        visited.add(state)
        
        u, last_color = state
        current_dist = dist[state]
        
        if u == t:
            return current_dist
        
        for v, color in adj[u]:
            new_state = (v, color)
            cost = 0 if color == last_color else 1
            new_dist = current_dist + cost
            
            if new_state not in dist or new_dist < dist[new_state]:
                dist[new_state] = new_dist
                if cost == 0:
                    dq.appendleft(new_state)
                else:
                    dq.append(new_state)
    
    return -1

t = int(input())
for _ in range(t):
    print(solve())
