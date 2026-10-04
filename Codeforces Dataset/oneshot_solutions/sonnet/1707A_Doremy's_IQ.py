import sys

def solve(n, q, a):
    # Count expensive contests (a[i] > q) from position i to end
    expensive_from = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        expensive_from[i] = expensive_from[i + 1] + (1 if a[i] > q else 0)
    
    # Find earliest position where we can afford all expensive contests from there
    start = n
    for k in range(n + 1):
        if expensive_from[k] <= q:
            start = k
            break
    
    # Simulate from start position to build result
    result = ['0'] * start
    current_q = q
    for i in range(start, n):
        if current_q > 0:
            result.append('1')
            if a[i] > current_q:
                current_q -= 1
        else:
            result.append('0')
    
    return ''.join(result)

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        q = int(input_data[idx + 1])
        idx += 2
        a = list(map(int, input_data[idx:idx + n]))
        idx += n
        print(solve(n, q, a))

if __name__ == '__main__':
    main()
