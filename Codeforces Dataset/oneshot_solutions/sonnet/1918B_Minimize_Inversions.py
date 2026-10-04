t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    pairs = sorted(zip(a, b))
    
    print(' '.join(str(p[0]) for p in pairs))
    print(' '.join(str(p[1]) for p in pairs))
