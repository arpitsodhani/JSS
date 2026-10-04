import sys

def fixed_matches(a, b, n):
    j = 0
    matches = 0
    
    for value in a:
        while j < n and b[j] <= value:
            j += 1
        
        if j < n:
            matches += 1
            j += 1
    
    return matches

def can_improve(x, a, b, n, base):
    i = 0
    j = 0
    matches = 0
    used_x = False
    
    while i < n - 1 or not used_x:
        if not used_x and (i == n - 1 or x <= a[i]):
            value = x
            used_x = True
        else:
            value = a[i]
            i += 1
        
        while j < n and b[j] <= value:
            j += 1
        
        if j < n:
            matches += 1
            j += 1
            
            if matches > base:
                return True
    
    return False

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n - 1]
        idx += n - 1
        
        b = data[idx:idx + n]
        idx += n
        
        a.sort()
        b.sort()
        
        base = fixed_matches(a, b, n)
        
        low = 1
        high = m
        good = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_improve(mid, a, b, n, base):
                good = mid
                low = mid + 1
            else:
                high = mid - 1
        
        normal_ops = n - base
        answers.append(str(good * (normal_ops - 1) + (m - good) * normal_ops))
    
    print('\n'.join(answers))

solve()
