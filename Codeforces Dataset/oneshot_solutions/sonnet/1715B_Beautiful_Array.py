import sys

def solve(n, k, b, s):
    min_sum = k * b
    max_sum = k * b + n * (k - 1)
    
    if s < min_sum or s > max_sum:
        return None
    
    result = [0] * n
    result[0] = k * b
    remaining = s - k * b
    
    for i in range(n):
        add = min(remaining, k - 1)
        result[i] += add
        remaining -= add
    
    return result

def main():
    data = sys.stdin.buffer.read().decode('utf-8').strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        b = int(data[idx + 2])
        s = int(data[idx + 3])
        idx += 4
        
        result = solve(n, k, b, s)
        if result is None:
            print(-1)
        else:
            print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
