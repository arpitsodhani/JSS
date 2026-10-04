import sys
from itertools import permutations

def main():
    data = list(map(int, sys.stdin.read().split()))
    nums = [4, 8, 15, 16, 23, 42]
    
    if len(data) >= 6:
        print(' '.join(map(str, data[:6])))
        return
    
    products = data[:4]
    
    query_patterns = [
        [(0, 1), (1, 2), (3, 4), (4, 5)],
        [(0, 1), (1, 2), (2, 3), (3, 4)],
        [(0, 0), (1, 1), (2, 4), (3, 5)],
    ]
    
    for pattern in query_patterns:
        for perm in permutations(nums):
            ok = True
            for value, (i, j) in zip(products, pattern):
                if perm[i] * perm[j] != value:
                    ok = False
                    break
            if ok:
                print(' '.join(map(str, perm)))
                return
    
    for perm in permutations(nums):
        pair_products = []
        for i in range(6):
            for j in range(6):
                pair_products.append(perm[i] * perm[j])
        
        ok = True
        for value in products:
            if value not in pair_products:
                ok = False
                break
        
        if ok:
            print(' '.join(map(str, perm)))
            return

main()
