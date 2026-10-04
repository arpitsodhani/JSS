import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []
    
    for _ in range(t):
        n, m, sx, sy, d = data[idx:idx + 5]
        idx += 5
        
        blocked_start_corner = sx - d <= 1 and sy - d <= 1
        blocked_end_corner = sx + d >= n and sy + d >= m
        blocked_all_rows = sx - d <= 1 and sx + d >= n
        blocked_all_cols = sy - d <= 1 and sy + d >= m
        
        if blocked_start_corner or blocked_end_corner or blocked_all_rows or blocked_all_cols:
            ans.append("-1")
        else:
            ans.append(str(n + m - 2))
    
    print("\n".join(ans))

if __name__ == "__main__":
    main()
