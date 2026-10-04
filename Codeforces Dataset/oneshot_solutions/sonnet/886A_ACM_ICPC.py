import sys
from itertools import combinations

def main():
    a = list(map(int, sys.stdin.read().split()))
    total = sum(a)
    
    for team in combinations(range(6), 3):
        if sum(a[i] for i in team) * 2 == total:
            print("YES")
            return
    
    print("NO")

main()
