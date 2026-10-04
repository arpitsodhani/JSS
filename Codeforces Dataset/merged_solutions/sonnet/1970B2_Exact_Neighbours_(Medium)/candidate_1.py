# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    a = [0] + data[1:1 + n]
    
    positions = [(0, 0)] * (n + 1)
    target = [1] * (n + 1)
    
    positions[1] = (1, 1)
    used_columns = {1}
    
    for i in range(2, n + 1):
        d = a[i]
        
        if d == 0:
            print("NO")
            return
        
        if d + 1 <= n and d + 1 not in used_columns:
            positions[i] = (d + 1, 1)
            used_columns.add(d + 1)
            target[i] = 1
        else:
            col = None
            for c in range(1, n + 1):
                if c not in used_columns:
                    col = c
                    break
            
            if col is None:
                print("NO")
                return
            
            found = False
            for j in range(1, i):
                x, y = positions[j]
                rem = d - abs(col - x)
                if rem >= 0:
                    for ny in (y + rem, y - rem):
                        if 1 <= ny <= n:
                            positions[i] = (col, ny)
                            used_columns.add(col)
                            target[i] = j
                            found = True
                            break
                if found:
                    break
            
            if not found:
                print("NO")
                return
    
    print("YES")
    for i in range(1, n + 1):
        print(positions[i][0], positions[i][1])
    print(" ".join(map(str, target[1:])))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
