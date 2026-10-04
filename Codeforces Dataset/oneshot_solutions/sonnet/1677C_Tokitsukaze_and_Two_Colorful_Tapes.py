from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Find position of each color on each tape
    pos1 = [0] * (n + 1)
    pos2 = [0] * (n + 1)
    
    for i in range(n):
        pos1[a[i]] = i
        pos2[b[i]] = i
    
    # Build graph: each color connects to colors it pairs with
    graph = defaultdict(list)
    for c in range(1, n + 1):
        graph[c].append(b[pos1[c]])
        graph[c].append(a[pos2[c]])
    
    # Find all cycles
    visited = [False] * (n + 1)
    cycles = []
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        
        cycle_len = 0
        prev = -1
        node = start
        
        while not visited[node]:
            visited[node] = True
            cycle_len += 1
            
            # Find next node (not the one we came from)
            next_node = -1
            for neighbor in graph[node]:
                if neighbor != prev:
                    next_node = neighbor
                    break
            
            if next_node == -1:
                break
            
            prev = node
            node = next_node
        
        cycles.append(cycle_len)
    
    # Sort cycles by length (descending) for greedy assignment
    cycles.sort(reverse=True)
    
    # Assign values: use extremes for each cycle
    total = 0
    left = 1
    right = n
    
    for cycle_len in cycles:
        if cycle_len == 1:
            left += 1
            continue
        
        half = cycle_len // 2
        contribution = cycle_len * (right - left - half + 1)
        total += contribution
        
        left += half
        right -= half
    
    print(total)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
