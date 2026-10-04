import sys

def ask(l, r):
    print("?", l, r, flush=True)
    return int(sys.stdin.readline())

def main():
    n_line = sys.stdin.readline().strip()
    if not n_line:
        return
    
    n = int(n_line)
    second = ask(1, n)
    
    if second == 1:
        side = "right"
    elif second == n:
        side = "left"
    else:
        side = "left" if ask(1, second) == second else "right"
    
    if side == "left":
        lo, hi = 1, second - 1
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            
            if ask(mid, second) == second:
                lo = mid
            else:
                hi = mid - 1
        
        print("!", lo, flush=True)
    else:
        lo, hi = second + 1, n
        
        while lo < hi:
            mid = (lo + hi) // 2
            
            if ask(second, mid) == second:
                hi = mid
            else:
                lo = mid + 1
        
        print("!", lo, flush=True)

if __name__ == "__main__":
    main()
