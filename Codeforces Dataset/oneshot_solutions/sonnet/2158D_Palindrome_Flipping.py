from collections import deque

def solve():
    n = int(input())
    s = input().strip()
    t = input().strip()
    
    if s == t:
        print(0)
        return
    
    # BFS
    queue = deque([(s, [])])
    visited = {s}
    
    while queue:
        curr, path = queue.popleft()
        
        if len(path) >= 2 * n:
            continue
        
        # Try all possible operations
        for l in range(n):
            for r in range(l + 1, n):
                substring = curr[l:r+1]
                if substring == substring[::-1]:  # palindrome
                    # Flip substring
                    new_s = curr[:l] + ''.join('1' if c == '0' else '0' for c in substring) + curr[r+1:]
                    
                    if new_s == t:
                        path.append((l + 1, r + 1))  # Convert to 1-indexed
                        print(len(path))
                        for op in path:
                            print(op[0], op[1])
                        return
                    
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append((new_s, path + [(l + 1, r + 1)]))

T = int(input())
for _ in range(T):
    solve()
