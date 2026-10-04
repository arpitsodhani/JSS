import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    a = data[idx:idx + n]
    idx += n
    
    add = 0
    out = []
    
    for _ in range(m):
        op = data[idx]
        idx += 1
        
        if op == 1:
            v = data[idx] - 1
            x = data[idx + 1]
            idx += 2
            a[v] = x - add
        elif op == 2:
            y = data[idx]
            idx += 1
            add += y
        else:
            q = data[idx] - 1
            idx += 1
            out.append(str(a[q] + add))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
