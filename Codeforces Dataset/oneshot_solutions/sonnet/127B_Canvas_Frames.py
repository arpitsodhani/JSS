import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    
    n = data[0]
    sticks = data[1:1 + n]
    
    pairs = 0
    for count in Counter(sticks).values():
        pairs += count // 2
    
    print(pairs // 2)

if __name__ == "__main__":
    main()
