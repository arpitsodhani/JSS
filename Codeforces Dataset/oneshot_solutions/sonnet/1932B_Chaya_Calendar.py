import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    results = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        year = 0
        for _ in range(n):
            a = data[idx]
            idx += 1
            year = ((year // a) + 1) * a
        
        results.append(str(year))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
