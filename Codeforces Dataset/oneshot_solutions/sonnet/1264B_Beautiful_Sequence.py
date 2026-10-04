def solve():
    a, b, c, d = map(int, input().split())
    
    if a + b + c + d == 0:
        print("YES")
        print()
        return
    
    seq = None
    
    # Pattern: 0 1 0 1 ... 1 2 3 2 3 ... 2
    if b == a + 1 and c == d + 1:
        seq = []
        for _ in range(a):
            seq += [0, 1]
        seq += [1, 2]
        for _ in range(d):
            seq += [3, 2]
    
    # Pattern: 0 1 0 1 ... 1 2 3 2 3 ... 3
    elif b == a + 1 and c == d and d > 0:
        seq = []
        for _ in range(a):
            seq += [0, 1]
        seq += [1]
        for _ in range(d):
            seq += [2, 3]
    
    # Pattern: 0 1 0 1 ... 0 1 2 3 2 3 ... 2
    elif b == a and c == d + 1 and a > 0:
        seq = []
        for _ in range(a):
            seq += [0, 1]
        seq += [2]
        for _ in range(d):
            seq += [3, 2]
    
    # Pattern: 0 1 0 1 ... 0 1 2 3 2 3 ... 3
    elif b == a and c == d and a > 0 and d > 0:
        seq = []
        for _ in range(a):
            seq += [0, 1]
        for _ in range(d):
            seq += [2, 3]
    
    # Pattern: 1 2 3 2 3 ... 2 (no 0s)
    elif a == 0 and b == 1 and c == d + 1:
        seq = [1, 2]
        for _ in range(d):
            seq += [3, 2]
    
    # Pattern: 1 2 3 2 3 ... 3 (no 0s)
    elif a == 0 and b == 1 and c == d and d > 0:
        seq = [1]
        for _ in range(d):
            seq += [2, 3]
    
    # Pattern: 0 1 0 1 ... 1 (no 2s, 3s)
    elif c == 0 and d == 0 and b == a + 1:
        seq = []
        for _ in range(a):
            seq += [0, 1]
        seq += [1]
    
    # Pattern: 0 1 0 1 ... 0 (no 2s, 3s)
    elif c == 0 and d == 0 and b + 1 == a and a > 0:
        seq = []
        for _ in range(b):
            seq += [0, 1]
        seq += [0]
    
    # Pattern: 2 3 2 3 ... 2 (no 0s, 1s)
    elif a == 0 and b == 0 and c == d + 1:
        seq = [2]
        for _ in range(d):
            seq += [3, 2]
    
    # Pattern: 2 3 2 3 ... 3 (no 0s, 1s)
    elif a == 0 and b == 0 and c + 1 == d and d > 0:
        seq = []
        for _ in range(c):
            seq += [2, 3]
        seq += [3]
    
    # Single elements
    elif a == 1 and b + c + d == 0:
        seq = [0]
    elif b == 1 and a + c + d == 0:
        seq = [1]
    elif c == 1 and a + b + d == 0:
        seq = [2]
    elif d == 1 and a + b + c == 0:
        seq = [3]
    
    if seq is not None:
        print("YES")
        print(' '.join(map(str, seq)))
    else:
        print("NO")

solve()
