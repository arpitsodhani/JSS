import sys

def solve():
    input_data = sys.stdin.buffer.read().decode().strip().split()
    idx = 0
    T = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(T):
        n = int(input_data[idx])
        s = int(input_data[idx + 1])
        t = int(input_data[idx + 2])
        idx += 3
        
        answer = n - min(s, t) + 1
        results.append(str(answer))
    
    print('\n'.join(results))

solve()
