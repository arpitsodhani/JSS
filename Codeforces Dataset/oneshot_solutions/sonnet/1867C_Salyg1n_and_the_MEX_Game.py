import sys

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

t = int(input())
for _ in range(t):
    n = int(input())
    s = set(map(int, input().split()))
    
    while True:
        m = mex(s)
        print(m)
        sys.stdout.flush()
        
        s.add(m)
        
        removed = int(input())
        if removed == -1:
            break
        
        s.discard(removed)
