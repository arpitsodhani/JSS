import sys
from math import comb
from collections import Counter

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]
    
    a.sort()
    chosen = a[:3]
    count_all = Counter(a)
    count_chosen = Counter(chosen)
    
    result = 1
    for value, need in count_chosen.items():
        result *= comb(count_all[value], need)
    
    print(result)

if __name__ == "__main__":
    main()
