import sys

def solve(n):
    if n == 1:
        return 0
    
    # Count powers of 2 and 3
    a = 0
    while n % 2 == 0:
        a += 1
        n //= 2
    
    b = 0
    while n % 3 == 0:
        b += 1
        n //= 3
    
    # If there are other prime factors
    if n > 1:
        return -1
    
    # If more 2s than 3s, impossible
    if a > b:
        return -1
    
    # Number of moves: multiply by 2 (b-a) times, then divide by 6 b times
    return 2 * b - a

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
