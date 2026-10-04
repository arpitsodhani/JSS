import sys

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def solve(n, s):
    if digit_sum(n) <= s:
        return 0
    
    original_n = n
    power = 1
    while digit_sum(n) > s:
        n = ((n // power) + 1) * power
        power *= 10
    
    return n - original_n

data = sys.stdin.read().split()
t = int(data[0])
idx = 1
for _ in range(t):
    n = int(data[idx])
    s = int(data[idx + 1])
    idx += 2
    print(solve(n, s))
