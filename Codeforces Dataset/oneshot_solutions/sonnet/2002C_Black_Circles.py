import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        circles = []
        for _ in range(n):
            x = int(input_data[idx])
            y = int(input_data[idx + 1])
            circles.append((x, y))
            idx += 2
        
        xs, ys, xt, yt = map(int, input_data[idx:idx+4])
        idx += 4
        
        # Distance squared from start to target
        D_sq = (xt - xs) ** 2 + (yt - ys) ** 2
        
        # Check if all circles are farther from target than we are
        can_reach = True
        for cx, cy in circles:
            dist_sq = (xt - cx) ** 2 + (yt - cy) ** 2
            if dist_sq <= D_sq:
                can_reach = False
                break
        
        results.append("YES" if can_reach else "NO")
    
    print('\n'.join(results))

solve()
