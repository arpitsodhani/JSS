# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def cross(ax, ay, bx, by, cx, cy):
    return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    red = []
    for _ in range(n):
        red.append((data[idx], data[idx + 1]))
        idx += 2
    
    blue = []
    for _ in range(m):
        blue.append((data[idx], data[idx + 1]))
        idx += 2
    
    if m == 0:
        print(n * (n - 1) * (n - 2) // 6)
        return
    
    all_blue = (1 << m) - 1
    left = [[0] * n for _ in range(n)]
    
    for i in range(n):
        ax, ay = red[i]
        for j in range(i + 1, n):
            bx, by = red[j]
            mask = 0
            for b, (cx, cy) in enumerate(blue):
                if cross(ax, ay, bx, by, cx, cy) > 0:
                    mask |= 1 << b
            
            left[i][j] = mask
            left[j][i] = all_blue ^ mask
    
    answer = 0
    
    for i in range(n - 2):
        ax, ay = red[i]
        left_i = left[i]
        
        for j in range(i + 1, n - 1):
            bx, by = red[j]
            left_j = left[j]
            mask_ij = left_i[j]
            mask_ji = left_j[i]
            
            for k in range(j + 1, n):
                cx, cy = red[k]
                
                if cross(ax, ay, bx, by, cx, cy) > 0:
                    inside = mask_ij & left_j[k] & left[k][i]
                else:
                    inside = mask_ji & left[k][j] & left_i[k]
                
                if inside == 0:
                    answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
