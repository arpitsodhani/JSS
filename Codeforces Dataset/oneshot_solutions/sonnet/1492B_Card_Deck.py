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
        
        p = data[idx:idx + n]
        idx += n
        
        pos = [0] * (n + 1)
        for i, x in enumerate(p):
            pos[x] = i
        
        result = []
        right = n - 1
        value = n
        
        while right >= 0:
            while pos[value] > right:
                value -= 1
            
            left = pos[value]
            result.extend(p[left:right + 1])
            right = left - 1
            value -= 1
        
        answers.append(' '.join(map(str, result)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
