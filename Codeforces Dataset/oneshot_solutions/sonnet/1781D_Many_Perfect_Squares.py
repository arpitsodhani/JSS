import sys
from math import isqrt

def get_divisors(n):
    if n == 0:
        return []
    divisors = []
    n = abs(n)
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def is_perfect_square(n):
    if n < 0:
        return False
    root = isqrt(n)
    return root * root == n

def count_squareness(a, x):
    count = 0
    for val in a:
        if is_perfect_square(val + x):
            count += 1
    return count

def solve(a):
    n = len(a)
    if n == 0:
        return 0
    
    candidates = set()
    candidates.add(0)
    
    for val in a:
        root = isqrt(val)
        if root * root < val:
            root += 1
        for k in range(root, min(root + 10, 10**9 + 1)):
            x = k * k - val
            if x > 10**18:
                break
            candidates.add(x)
    
    for i in range(n):
        for j in range(i + 1, n):
            ai, aj = a[i], a[j]
            if ai < aj:
                ai, aj = aj, ai
            
            diff = ai - aj
            if diff == 0:
                continue
            
            divisors = get_divisors(diff)
            
            for d in divisors:
                sum_pq = diff // d
                
                if (d + sum_pq) % 2 != 0:
                    continue
                
                p = (d + sum_pq) // 2
                q = (sum_pq - d) // 2
                
                if p < 1 or q < 0:
                    continue
                
                x = p * p - ai
                
                if 0 <= x <= 10**18:
                    candidates.add(x)
    
    max_squareness = 0
    for x in candidates:
        squareness = count_squareness(a, x)
        max_squareness = max(max_squareness, squareness)
    
    return max_squareness

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        result = solve(a)
        print(result)

if __name__ == "__main__":
    main()
