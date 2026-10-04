import sys
sys.setrecursionlimit(200000)

def solve():
    n = int(input())
    k = [0] + list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    start = int(input())
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Root tree at start
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        v, parent = stack.pop()
        for u in adj[v]:
            if u != parent and not visited[u]:
                visited[u] = True
                children[v].append(u)
                stack.append((u, v))
    
    dp = [[0, 0] for _ in range(n + 1)]
    eat_at = [[0, 0] for _ in range(n + 1)]
    
    def dfs(v):
        if not children[v]:
            return
        
        for u in children[v]:
            dfs(u)
        
        for entered in [0, 1]:
            capacity = k[v] - entered
            if capacity < 0:
                continue
            
            # For each child, calculate max round trips and value per trip
            child_info = []
            for u in children[v]:
                cost_per_trip = eat_at[u][1] + 1
                if cost_per_trip > 0 and k[u] >= cost_per_trip:
                    max_trips = k[u] // cost_per_trip
                    value_per_trip = dp[u][1] + 2
                    child_info.append((value_per_trip, max_trips))
            
            # Greedily select trips in order of value
            child_info.sort(reverse=True)
            
            total_eaten = 0
            total_trips = 0
            for value, max_count in child_info:
                trips = min(max_count, capacity - total_trips)
                total_eaten += trips * value
                total_trips += trips
                if total_trips >= capacity:
                    break
            
            dp[v][entered] = total_eaten
            eat_at[v][entered] = total_trips
    
    dfs(start)
    print(dp[start][0])

solve()
