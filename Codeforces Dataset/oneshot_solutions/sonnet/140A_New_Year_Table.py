import sys
import math

def main():
    n, R, r = map(int, sys.stdin.read().split())
    
    if n == 1:
        print("YES" if r <= R else "NO")
        return
    
    if 2 * r > R:
        print("NO")
        return
    
    can_fit = math.sin(math.pi / n) + 1e-12 >= r / (R - r)
    print("YES" if can_fit else "NO")

main()
