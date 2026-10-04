import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, l, r = data[0], data[1], data[2]
    idx = 3
    
    a = data[idx:idx + n]
    idx += n
    b = data[idx:idx + n]
    
    l -= 1
    r -= 1
    
    for i in range(n):
        if i < l or i > r:
            if a[i] != b[i]:
                print("LIE")
                return
    
    if Counter(a[l:r + 1]) == Counter(b[l:r + 1]):
        print("TRUTH")
    else:
        print("LIE")

if __name__ == "__main__":
    main()
