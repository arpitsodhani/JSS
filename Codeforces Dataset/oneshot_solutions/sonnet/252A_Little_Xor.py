import sys

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    max_xor = 0
    
    for i in range(n):
        xor_val = 0
        for j in range(i, n):
            xor_val ^= a[j]
            max_xor = max(max_xor, xor_val)
    
    print(max_xor)

solve()
