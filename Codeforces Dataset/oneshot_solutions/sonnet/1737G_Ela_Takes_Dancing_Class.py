import sys

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    q = int(data[idx + 2])
    idx += 3
    
    a = [int(data[idx + i]) for i in range(n)]
    idx += n
    
    s = data[idx]
    idx += 1
    
    for _ in range(q):
        d = int(data[idx])
        query_idx = int(data[idx + 1]) - 1
        idx += 2
        
        # Simulate choreography with energy d
        pos = a[:]
        movable = [s[i] == '1' for i in range(n)]
        
        # Each movable dancer moves once, in leftmost order
        for _ in range(m):
            # Find leftmost movable dancer
            best = -1
            best_pos = float('inf')
            for i in range(n):
                if movable[i] and pos[i] < best_pos:
                    best = i
                    best_pos = pos[i]
            
            if best == -1:
                break
            
            # Find next obstacle (any dancer to the right)
            limit = float('inf')
            for j in range(n):
                if j != best and pos[j] > pos[best]:
                    limit = min(limit, pos[j])
            
            # Move as far as possible with energy d
            if limit == float('inf'):
                pos[best] += d
            else:
                pos[best] = min(pos[best] + d, limit - 1)
            
            # Mark this dancer as no longer movable (moved once)
            movable[best] = False
        
        print(pos[query_idx])

if __name__ == "__main__":
    main()
