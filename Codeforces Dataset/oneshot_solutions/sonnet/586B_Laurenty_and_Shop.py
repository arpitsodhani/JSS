import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    top = data[idx:idx + n - 1]
    idx += n - 1
    
    bottom = data[idx:idx + n - 1]
    idx += n - 1
    
    cross = data[idx:idx + n]
    
    top_prefix = [0] * n
    for i in range(1, n):
        top_prefix[i] = top_prefix[i - 1] + top[i - 1]
    
    bottom_suffix = [0] * n
    for i in range(n - 2, -1, -1):
        bottom_suffix[i] = bottom_suffix[i + 1] + bottom[i]
    
    best = float('inf')
    for i in range(n):
        cost = top_prefix[i] + cross[i] + bottom_suffix[i]
        best = min(best, cost)
    
    print(2 * best)

if __name__ == "__main__":
    main()
