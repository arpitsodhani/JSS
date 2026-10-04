import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    k = data[1]
    a = data[2:2 + n]
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    
    best = 0.0
    for left in range(n):
        for right in range(left + k, n + 1):
            total = prefix[right] - prefix[left]
            length = right - left
            best = max(best, total / length)
    
    print(best)

if __name__ == "__main__":
    main()
