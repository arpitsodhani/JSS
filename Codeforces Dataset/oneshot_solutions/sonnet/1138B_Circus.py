import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    c = data[1]
    a = data[2]
    
    groups = {
        (0, 0): [],
        (0, 1): [],
        (1, 0): [],
        (1, 1): []
    }
    
    for i in range(n):
        groups[(int(c[i]), int(a[i]))].append(i + 1)
    
    cnt00 = len(groups[(0, 0)])
    cnt01 = len(groups[(0, 1)])
    cnt10 = len(groups[(1, 0)])
    cnt11 = len(groups[(1, 1)])
    
    half = n // 2
    total_acrobats = cnt01 + cnt11
    
    for x11 in range(cnt11 + 1):
        need = total_acrobats - 2 * x11
        x00 = half - x11 - need
        
        if need < 0 or x00 < 0 or x00 > cnt00:
            continue
        
        low_x01 = max(0, need - cnt10)
        high_x01 = min(cnt01, need)
        
        if low_x01 <= high_x01:
            x01 = low_x01
            x10 = need - x01
            
            result = []
            result += groups[(0, 0)][:x00]
            result += groups[(0, 1)][:x01]
            result += groups[(1, 0)][:x10]
            result += groups[(1, 1)][:x11]
            
            print(' '.join(map(str, result)))
            return
    
    print(-1)

if __name__ == "__main__":
    main()
