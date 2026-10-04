# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    pairs = data[1:]
    
    count = [0] * (n + 1)
    for i in range(0, 2 * (n - 1), 2):
        a = pairs[i]
        b = pairs[i + 1]
        
        if a != n and b != n:
            print("NO")
            return
        
        x = a + b - n
        if x == n:
            print("NO")
            return
        count[x] += 1
    
    used = [False] * (n + 1)
    for i in range(1, n):
        if count[i] > 0:
            used[i] = True
    
    free = []
    for i in range(1, n):
        if not used[i]:
            heapq.heappush(free, i)
    
    edges = []
    roots = []
    
    for x in range(1, n):
        if count[x] == 0:
            continue
        
        chain = []
        for _ in range(count[x] - 1):
            if not free or free[0] > x:
                print("NO")
                return
            chain.append(heapq.heappop(free))
        
        chain.append(x)
        roots.append(chain[0])
        
        for i in range(len(chain) - 1):
            edges.append((chain[i], chain[i + 1]))
    
    for v in roots:
        edges.append((n, v))
    
    if len(edges) != n - 1:
        print("NO")
        return
    
    print("YES")
    for a, b in edges:
        print(a, b)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
