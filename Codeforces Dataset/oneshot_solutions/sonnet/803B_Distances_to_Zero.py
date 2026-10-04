import sys

def solve():
    input_data = sys.stdin.buffer.read().decode('ascii').split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # Initialize result array with large number
    INF = 10**9
    result = [INF] * n
    
    # Left to right pass
    last_zero = -1
    for i in range(n):
        if a[i] == 0:
            last_zero = i
            result[i] = 0
        elif last_zero >= 0:
            result[i] = i - last_zero
    
    # Right to left pass
    last_zero = -1
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last_zero = i
            result[i] = 0
        elif last_zero >= 0:
            result[i] = min(result[i], last_zero - i)
    
    print(' '.join(map(str, result)))

solve()
