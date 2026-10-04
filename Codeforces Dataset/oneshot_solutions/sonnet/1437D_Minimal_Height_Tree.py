def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        return 0
    
    level_start = 0  # start index of current level's parents
    level_end = 1    # end index of current level's parents
    child_idx = 1    # next vertex to assign as a child
    current_depth = 0
    
    while child_idx < n:
        current_depth += 1
        next_level_start = child_idx
        
        # Process all parents at current level
        for parent_idx in range(level_start, level_end):
            if child_idx >= n:
                break
            
            # Assign first child to this parent
            prev_val = a[child_idx]
            child_idx += 1
            
            # Keep assigning children while values are ascending
            while child_idx < n and a[child_idx] > prev_val:
                prev_val = a[child_idx]
                child_idx += 1
        
        level_start = next_level_start
        level_end = child_idx
    
    return current_depth

t = int(input())
for _ in range(t):
    print(solve())
