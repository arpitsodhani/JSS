# CLAUSE: setup_environment
import sys
from bisect import bisect_left, bisect_right
from collections import deque

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    heroes = []
    for i in range(1, m + 1):
        s = data[idx]
        h = data[idx + 1]
        idx += 2
        heroes.append((s, h, i))
    
    cells = [0] + data[idx:idx + n]
    heroes.sort()
    
    positions = [x[0] for x in heroes]
    health = [x[1] for x in heroes]
    ids = [x[2] for x in heroes]
    
    can = [[False] * (n + 1) for _ in range(m)]
    
    for i in range(m):
        start = positions[i]
        for target in range(1, n + 1):
            hp = health[i]
            ok = True
            step = 1 if target >= start else -1
            cur = start
            
            while True:
                hp += cells[cur]
                if hp < 0:
                    ok = False
                    break
                if cur == target:
                    break
                cur += step
            
            can[i][target] = ok
    
    for rally in range(1, n + 1):
        parent = [[None] * m for _ in range(m)]
        q = deque()
        
        for i in range(m):
            if not can[i][rally]:
                continue
            
            left = min(positions[i], rally)
            right = max(positions[i], rally)
            lo = bisect_left(positions, left)
            hi = bisect_right(positions, right) - 1
            
            if parent[lo][hi] is None:
                parent[lo][hi] = (-1, -1, i)
                q.append((lo, hi))
        
        while q:
            lo, hi = q.popleft()
            
            if lo == 0 and hi == m - 1:
                order = []
                cur_lo, cur_hi = lo, hi
                
                while True:
                    prev_lo, prev_hi, hero = parent[cur_lo][cur_hi]
                    order.append(hero)
                    if prev_lo == -1:
                        break
                    cur_lo, cur_hi = prev_lo, prev_hi
                
                order.reverse()
                used = set(order)
                for i in range(m):
                    if i not in used:
                        order.append(i)
                
                print(rally)
                print(' '.join(str(ids[i]) for i in order))
                return
            
            left_cell = min(rally, positions[lo])
            right_cell = max(rally, positions[hi])
            
            target = left_cell - 1
            if target >= 1:
                for i in range(lo):
                    if can[i][target] and parent[i][hi] is None:
                        parent[i][hi] = (lo, hi, i)
                        q.append((i, hi))
            
            target = right_cell + 1
            if target <= n:
                for i in range(hi + 1, m):
                    if can[i][target] and parent[lo][i] is None:
                        parent[lo][i] = (lo, hi, i)
                        q.append((lo, i))
    
    print(-1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
