import sys

def count_inversions(a):
    count = 0
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                count += 1
    return count

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    original_inv = count_inversions(a)
    
    min_inv = original_inv
    count_ways = 0
    
    for i in range(n):
        for j in range(i+1, n):
            # Calculate change in inversions when swapping positions i and j
            if a[i] < a[j]:
                # Count k with i < k < j and a[i] < a[k] < a[j]
                cnt = sum(1 for k in range(i+1, j) if a[i] < a[k] < a[j])
                delta = 1 + 2 * cnt
            else:  # a[i] > a[j]
                # Count k with i < k < j and a[j] < a[k] < a[i]
                cnt = sum(1 for k in range(i+1, j) if a[j] < a[k] < a[i])
                delta = -1 - 2 * cnt
            
            new_inv = original_inv + delta
            
            if new_inv < min_inv:
                min_inv = new_inv
                count_ways = 1
            elif new_inv == min_inv:
                count_ways += 1
    
    print(min_inv, count_ways)

solve()
