import sys

def construct(n):
    if n == 1:
        return [1, 1]
    
    result = [0] * (2 * n + 1)
    smaller = construct(n // 2)
    
    for i, value in enumerate(smaller, 1):
        result[2 * i] = 2 * value
    
    if n % 2 == 0:
        for x in range(1, n, 2):
            result[n - x] = x
            result[n + x] = x
    else:
        result[n] = n
        result[2 * n] = n
        
        for x in range(3, n, 2):
            result[n - x - 1] = x
            result[n + x - 1] = x
        
        for i in range(1, 2 * n + 1):
            if result[i] == 0:
                result[i] = 1
    
    return result[1:]

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    
    output = []
    for i in range(1, t + 1):
        n = int(data[i])
        answer = construct(n)
        output.append(' '.join(map(str, answer)))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
