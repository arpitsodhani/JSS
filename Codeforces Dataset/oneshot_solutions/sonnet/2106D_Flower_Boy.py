import sys

def can_collect(garden, requirements):
    m = len(requirements)
    collected = 0
    for flower in garden:
        if collected < m and flower >= requirements[collected]:
            collected += 1
    return collected == m

def is_feasible(a, b, k):
    n = len(a)
    m = len(b)
    
    for pos in range(n + 1):
        collected = 0
        for i in range(n + 1):
            if i == pos:
                flower = k
            elif i < pos:
                flower = a[i]
            else:
                flower = a[i - 1]
            
            if collected < m and flower >= b[collected]:
                collected += 1
                if collected == m:
                    return True
    
    return False

def solve(n, m, a, b):
    if m == 0:
        return 0
    
    if can_collect(a, b):
        return 0
    
    max_b = max(b)
    if not is_feasible(a, b, max_b):
        return -1
    
    left, right = 1, max_b
    result = max_b
    
    while left <= right:
        mid = (left + right) // 2
        if is_feasible(a, b, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

def main():
    data = sys.stdin.buffer.read().decode('utf-8').strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + m]))
        idx += m
        results.append(solve(n, m, a, b))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
