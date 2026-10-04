import sys

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(T):
        n = int(data[idx])
        x = int(data[idx + 1])
        t = int(data[idx + 2])
        idx += 3
        
        k = t // x
        if k >= n:
            ans = n * (n - 1) // 2
        else:
            ans = k * (2 * n - k - 1) // 2
        results.append(ans)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
