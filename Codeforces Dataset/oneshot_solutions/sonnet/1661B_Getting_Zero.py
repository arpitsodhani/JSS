import sys
from collections import deque

MOD = 32768

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    numbers = data[1:1 + n]
    
    dist = [-1] * MOD
    dist[0] = 0
    q = deque([0])
    
    while q:
        v = q.popleft()
        
        prev = (v - 1) % MOD
        if dist[prev] == -1:
            dist[prev] = dist[v] + 1
            q.append(prev)
        
        if v % 2 == 0:
            prev1 = v // 2
            prev2 = prev1 + MOD // 2
            
            if dist[prev1] == -1:
                dist[prev1] = dist[v] + 1
                q.append(prev1)
            
            if dist[prev2] == -1:
                dist[prev2] = dist[v] + 1
                q.append(prev2)
    
    print(' '.join(str(dist[x]) for x in numbers))

if __name__ == "__main__":
    main()
