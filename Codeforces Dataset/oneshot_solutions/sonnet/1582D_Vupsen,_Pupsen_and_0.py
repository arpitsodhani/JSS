import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        
        b = [0] * n
        start = 0
        
        if n % 2 == 1:
            x, y, z = a[0], a[1], a[2]
            
            if x + y != 0:
                b[0] = z
                b[1] = z
                b[2] = -(x + y)
            elif x + z != 0:
                b[0] = y
                b[1] = -(x + z)
                b[2] = y
            else:
                b[0] = -(y + z)
                b[1] = x
                b[2] = x
            
            start = 3
        
        for i in range(start, n, 2):
            b[i] = a[i + 1]
            b[i + 1] = -a[i]
        
        out.append(' '.join(map(str, b)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
