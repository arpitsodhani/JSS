import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    results = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        arr = data[idx:idx + n]
        idx += n
        
        results.append(str(max(arr) - min(arr)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
