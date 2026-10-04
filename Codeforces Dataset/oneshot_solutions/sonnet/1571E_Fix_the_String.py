def solve():
    n = int(input())
    s = input().strip()
    a = input().strip()
    
    patterns = ["(())", "()()"]
    
    # Find all constraints
    constraints = []
    for i in range(len(a)):
        if a[i] == '1':
            constraints.append(i)
    
    if not constraints:
        print(0)
        return
    
    k = len(constraints)
    min_changes = float('inf')
    
    # Try all 2^k combinations
    for mask in range(1 << k):
        # Build the target string based on this combination
        target = [None] * n
        valid = True
        
        for idx, pos in enumerate(constraints):
            pattern_idx = (mask >> idx) & 1
            pattern = patterns[pattern_idx]
            
            for j in range(4):
                if target[pos + j] is None:
                    target[pos + j] = pattern[j]
                elif target[pos + j] != pattern[j]:
                    valid = False
                    break
            
            if not valid:
                break
        
        if not valid:
            continue
        
        # Count changes (only for positions that are set by constraints)
        changes = 0
        for i in range(n):
            if target[i] is not None and target[i] != s[i]:
                changes += 1
        
        min_changes = min(min_changes, changes)
    
    if min_changes == float('inf'):
        print(-1)
    else:
        print(min_changes)

t = int(input())
for _ in range(t):
    solve()
