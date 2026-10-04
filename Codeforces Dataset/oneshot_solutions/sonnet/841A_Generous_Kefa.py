import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    
    counts = Counter(s)
    if max(counts.values()) <= k:
        print("YES")
    else:
        print("NO")

main()
