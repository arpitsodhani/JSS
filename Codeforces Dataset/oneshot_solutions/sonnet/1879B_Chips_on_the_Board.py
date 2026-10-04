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
        b = data[idx:idx + n]
        idx += n
        
        answer = min(sum(a) + n * min(b), sum(b) + n * min(a))
        out.append(str(answer))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
