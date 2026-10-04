import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        # Kadane's algorithm for maximum subarray sum
        max_ending = 0
        max_so_far = float('-inf')
        
        for x in a:
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)
        
        print(max_so_far)

solve()
