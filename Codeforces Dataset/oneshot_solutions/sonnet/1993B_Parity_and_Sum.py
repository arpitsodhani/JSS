def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    odds = [x for x in a if x % 2 == 1]
    evens = [x for x in a if x % 2 == 0]
    
    if len(odds) == 0 or len(evens) == 0:
        return 0
    
    max_odd = max(odds)
    evens.sort()
    
    operations = 0
    for e in evens:
        if e >= max_odd:
            max_odd = max_odd + e
            operations += 1
        max_odd = max_odd + e
        operations += 1
    
    return operations

t = int(input())
for _ in range(t):
    print(solve())
