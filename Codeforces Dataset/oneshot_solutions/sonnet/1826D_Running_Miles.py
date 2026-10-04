import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        b = data[idx:idx + n]
        idx += n
        
        left_best = [0] * n
        best = b[0] + 1
        for i in range(n):
            best = max(best, b[i] + i + 1)
            left_best[i] = best
        
        right_best = [0] * n
        best = b[-1] - n
        for i in range(n - 1, -1, -1):
            best = max(best, b[i] - (i + 1))
            right_best[i] = best
        
        result = -10**30
        for j in range(1, n - 1):
            value = left_best[j - 1] + b[j] + right_best[j + 1]
            result = max(result, value)
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
