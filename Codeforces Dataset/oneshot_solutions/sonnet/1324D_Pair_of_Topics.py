import sys
from bisect import bisect_right

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    b = data[1 + n:1 + 2 * n]
    
    diff = [a[i] - b[i] for i in range(n)]
    diff.sort()
    
    ans = 0
    for i in range(n):
        pos = bisect_right(diff, -diff[i], i + 1)
        ans += n - pos
    
    print(ans)

if __name__ == "__main__":
    main()
