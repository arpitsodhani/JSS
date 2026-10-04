# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    points = []
    idx = 1
    
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        points.append((x, y))
    
    if n % 2 == 1:
        print("NO")
        return
    
    half = n // 2
    sx = points[0][0] + points[half][0]
    sy = points[0][1] + points[half][1]
    
    for i in range(1, half):
        if points[i][0] + points[i + half][0] != sx:
            print("NO")
            return
        if points[i][1] + points[i + half][1] != sy:
            print("NO")
            return
    
    print("YES")

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
