import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        r = data[idx + 2]
        c = data[idx + 3]
        idx += 4
        
        pos = (r - 1) * m + c
        moves = n * m - pos
        row_changes = n - r
        
        out.append(str(moves + row_changes * (m - 1)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
