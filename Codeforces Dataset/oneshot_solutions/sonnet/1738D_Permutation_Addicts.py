def solve():
    n = int(input())
    b = [0] + list(map(int, input().split()))
    
    # Classify elements into L (<=k) and R (>k)
    L = set()
    R = set()
    
    for i in range(1, n+1):
        if b[i] == n+1:
            L.add(i)
        elif b[i] == 0:
            R.add(i)
    
    # Propagate classification
    changed = True
    while changed:
        changed = False
        for i in range(1, n+1):
            if i in L or i in R:
                continue
            if 1 <= b[i] <= n:
                if b[i] in L:
                    R.add(i)
                    changed = True
                elif b[i] in R:
                    L.add(i)
                    changed = True
    
    k = len(L)
    
    # Build permutation
    perm = []
    placed = set()
    last_L = None
    last_R = None
    
    # Find starting elements
    starts = [i for i in range(1, n+1) if b[i] == 0 or b[i] == n+1]
    
    # Sort by number of dependents (ascending) - place most depended-on last
    def count_dependents(e):
        return sum(1 for i in range(1, n+1) if b[i] == e)
    
    starts.sort(key=count_dependents)
    
    # Place starting elements
    for e in starts:
        perm.append(e)
        placed.add(e)
        if e in L:
            last_L = e
        else:
            last_R = e
    
    # Place remaining elements
    while len(perm) < n:
        for i in range(1, n+1):
            if i in placed:
                continue
            if i in L:
                if b[i] == last_R:
                    perm.append(i)
                    placed.add(i)
                    last_L = i
                    break
            else:
                if b[i] == last_L:
                    perm.append(i)
                    placed.add(i)
                    last_R = i
                    break
    
    print(k)
    print(' '.join(map(str, perm)))

t = int(input())
for _ in range(t):
    solve()
