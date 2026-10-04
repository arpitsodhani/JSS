# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    w = int(data[1])
    m = int(data[2])
    
    g = gcd(n, m)
    
    if m > 2 * n or (m // g) > 2:
        print("NO")
        return
    
    print("YES")
    
    if m <= n:
        total = n * w
        need = total / m
        
        bottle = 1
        left = float(w)
        
        for _ in range(m):
            cur = need
            parts = []
            
            while cur > 1e-9:
                take = min(left, cur)
                parts.append((bottle, take))
                cur -= take
                left -= take
                
                if left < 1e-9:
                    bottle += 1
                    left = float(w)
            
            print(len(parts), end="")
            for b, amount in parts:
                print(f" {b} {amount:.6f}", end="")
            print()
    else:
        used_cups = [[] for _ in range(m)]
        cup = 0
        need = n * w / m
        half = w - need
        
        for bottle in range(1, n + 1):
            if half < 1e-9:
                used_cups[cup].append((bottle, need))
                cup += 1
            else:
                used_cups[cup].append((bottle, need))
                cup += 1
                used_cups[cup].append((bottle, half))
                
                rem = need - half
                if rem > 1e-9:
                    used_cups[cup].append((bottle, rem))
                    cup += 1
        
        for parts in used_cups:
            print(len(parts), end="")
            for b, amount in parts:
                print(f" {b} {amount:.6f}", end="")
            print()

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
