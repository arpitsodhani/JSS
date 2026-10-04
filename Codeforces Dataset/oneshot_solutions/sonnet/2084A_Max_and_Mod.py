import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        if n % 2 == 0:
            print(-1)
        else:
            result = [n] + list(range(1, n))
            print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
