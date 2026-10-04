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
        
        a = data[idx:idx + n]
        idx += n
        
        ops = 0
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                ops += a[i] - a[i + 1]
        
        answers.append(str(ops))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
