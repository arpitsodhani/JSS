import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = [0] + data[1:1 + n]
    
    for x in a[1:]:
        if x < 1 or x > n:
            print(-1)
            return
    
    indeg = [0] * (n + 1)
    for i in range(1, n + 1):
        indeg[a[i]] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
    
    state = [-1] * (n + 1)
    has_chosen_child = [False] * (n + 1)
    removed = [False] * (n + 1)
    
    while q:
        v = q.popleft()
        removed[v] = True
        
        state[v] = 0 if has_chosen_child[v] else 1
        
        to = a[v]
        if state[v] == 1:
            has_chosen_child[to] = True
        
        indeg[to] -= 1
        if indeg[to] == 0:
            q.append(to)
    
    seen = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if removed[i] or seen[i]:
            continue
        
        cycle = []
        v = i
        while not seen[v]:
            seen[v] = True
            cycle.append(v)
            v = a[v]
        
        start = -1
        for v in cycle:
            if has_chosen_child[v]:
                start = v
                break
        
        if start == -1:
            if len(cycle) % 2 == 1:
                print(-1)
                return
            
            cur = cycle[0]
            state[cur] = 0
            nxt = a[cur]
            while nxt != cycle[0]:
                state[nxt] = 1 - state[cur]
                cur = nxt
                nxt = a[cur]
        else:
            cur = start
            state[cur] = 0
            nxt = a[cur]
            while nxt != start:
                if has_chosen_child[nxt]:
                    state[nxt] = 0
                else:
                    state[nxt] = 1 - state[cur]
                cur = nxt
                nxt = a[cur]
    
    result = []
    for i in range(1, n + 1):
        if state[i] == 1:
            result.append(a[i])
    
    print(len(result))
    if result:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
