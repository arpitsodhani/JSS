import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    
    order = sorted(range(n), key=lambda i: (a[i], i))
    
    rank_at_pos = [0] * n
    for r, pos in enumerate(order):
        rank_at_pos[pos] = r
    
    pos_of_rank = [0] * n
    for pos, r in enumerate(rank_at_pos):
        pos_of_rank[r] = pos
    
    q = deque()
    for r in range(n - 1):
        if pos_of_rank[r] > pos_of_rank[r + 1]:
            q.append(r)
    
    answer = []
    
    while q:
        r = q.popleft()
        if r < 0 or r >= n - 1:
            continue
        if pos_of_rank[r] < pos_of_rank[r + 1]:
            continue
        
        p1 = pos_of_rank[r]
        p2 = pos_of_rank[r + 1]
        
        u, v = sorted((p1, p2))
        answer.append((u + 1, v + 1))
        
        rank_at_pos[p1], rank_at_pos[p2] = rank_at_pos[p2], rank_at_pos[p1]
        pos_of_rank[r], pos_of_rank[r + 1] = pos_of_rank[r + 1], pos_of_rank[r]
        
        for nr in (r - 1, r, r + 1):
            if 0 <= nr < n - 1 and pos_of_rank[nr] > pos_of_rank[nr + 1]:
                q.append(nr)
    
    out = [str(len(answer))]
    out.extend(f"{u} {v}" for u, v in answer)
    print('\n'.join(out))

if __name__ == "__main__":
    main()
