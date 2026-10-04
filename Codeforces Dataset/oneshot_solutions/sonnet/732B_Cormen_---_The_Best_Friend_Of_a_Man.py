import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    a = [int(data[idx + i]) for i in range(n)]
    
    # Initialize b as a copy of a
    b = a[:]
    
    # Adjust b to satisfy the constraint
    for i in range(n - 1):
        if b[i] + b[i+1] < k:
            b[i+1] = k - b[i]
    
    # Calculate additional walks
    additional = sum(b[i] - a[i] for i in range(n))
    
    # Output
    print(additional)
    print(' '.join(map(str, b)))

solve()
