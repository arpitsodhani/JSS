import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    grid = []
    for i in range(n):
        grid.append(input_data[idx])
        idx += 1
    
    MOD = 10**9 + 7
    
    # Initial rock positions (0-indexed)
    initial_rocks = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'R':
                initial_rocks.add((i, j))
    
    @lru_cache(maxsize=None)
    def dp(x, y, rocks):
        if x == n - 1 and y == m - 1:
            return 1
        
        result = 0
        
        # Try moving right to (x, y+1)
        if y + 1 < m:
            new_rocks = set(rocks)
            can_move = True
            
            # Count consecutive rocks starting from (x, y+1)
            push_count = 0
            check_y = y + 1
            while check_y < m and (x, check_y) in new_rocks:
                push_count += 1
                check_y += 1
            
            if push_count > 0:
                # Need to push rocks, the last rock will be at (x, y+1+push_count)
                if y + 1 + push_count >= m:
                    can_move = False
                else:
                    # Shift rocks one position to the right
                    for i in range(push_count):
                        new_rocks.remove((x, y + 1 + i))
                    for i in range(push_count):
                        new_rocks.add((x, y + 2 + i))
            
            if can_move:
                result = (result + dp(x, y + 1, frozenset(new_rocks))) % MOD
        
        # Try moving down to (x+1, y)
        if x + 1 < n:
            new_rocks = set(rocks)
            can_move = True
            
            # Count consecutive rocks starting from (x+1, y)
            push_count = 0
            check_x = x + 1
            while check_x < n and (check_x, y) in new_rocks:
                push_count += 1
                check_x += 1
            
            if push_count > 0:
                # Need to push rocks, the last rock will be at (x+1+push_count, y)
                if x + 1 + push_count >= n:
                    can_move = False
                else:
                    # Shift rocks one position down
                    for i in range(push_count):
                        new_rocks.remove((x + 1 + i, y))
                    for i in range(push_count):
                        new_rocks.add((x + 2 + i, y))
            
            if can_move:
                result = (result + dp(x + 1, y, frozenset(new_rocks))) % MOD
        
        return result
    
    # Check if starting position has a rock
    if (0, 0) in initial_rocks:
        print(0)
    else:
        print(dp(0, 0, frozenset(initial_rocks)))

solve()
