import sys

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        result = 0
        for i in range(n):
            a = int(input_data[idx])
            idx += 1
            result |= a
        
        print(result)

solve()
