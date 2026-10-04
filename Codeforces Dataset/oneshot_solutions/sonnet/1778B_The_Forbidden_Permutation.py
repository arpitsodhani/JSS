import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    t = data[idx]
    idx += 1
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        d = data[idx + 2]
        idx += 3
        
        p = data[idx:idx + n]
        idx += n
        
        a = data[idx:idx + m]
        idx += m
        
        pos = [0] * (n + 1)
        for i, value in enumerate(p):
            pos[value] = i
        
        result = n
        
        for i in range(m - 1):
            left = pos[a[i]]
            right = pos[a[i + 1]]
            
            if left > right or right > left + d:
                result = 0
                break
            
            gap = right - left
            result = min(result, gap)
            
            if d < n - 1:
                result = min(result, d + 1 - gap)
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
