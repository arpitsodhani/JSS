import sys

def solve():
    input = sys.stdin.read().strip().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        s = input[idx]
        idx += 1
        
        # Count inversions
        inversions = 0
        ones_count = 0
        for c in s:
            if c == '1':
                ones_count += 1
            else:  # c == '0'
                inversions += ones_count
        
        # Alice wins if inversions % 4 != 0
        if inversions % 4 == 0:
            results.append("Bob")
        else:
            results.append("Alice")
    
    print('\n'.join(results))

solve()
