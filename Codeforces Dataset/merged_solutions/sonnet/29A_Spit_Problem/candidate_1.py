# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    camels = []
    idx = 1
    
    for _ in range(n):
        x = data[idx]
        d = data[idx + 1]
        idx += 2
        camels.append((x, d))
    
    seen = set(camels)
    
    for x, d in camels:
        if d != 0 and (x + d, -d) in seen:
            print("YES")
            return
    
    print("NO")

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
