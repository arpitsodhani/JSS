import sys

def main():
    n, k, t = map(int, sys.stdin.read().split())
    
    total = n * k * t // 100
    result = []
    
    for _ in range(n):
        cur = min(k, total)
        result.append(cur)
        total -= cur
    
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
