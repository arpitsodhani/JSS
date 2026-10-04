import sys

def solve():
    input_data = sys.stdin.buffer.read().decode().strip().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        k = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        pos = m % (3 * k)
        if pos < 2 * k:
            print(2 * k - pos)
        else:
            print(0)

solve()
