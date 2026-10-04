import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    a = 1 << 29
    b = 1 << 30
    
    answers = []
    for i in range(1, t + 1):
        n = int(data[i])
        
        result = []
        x = 0
        for v in range(1, n - 2):
            result.append(v)
            x ^= v
        
        result.append(a)
        result.append(b)
        result.append(x ^ a ^ b)
        
        answers.append(' '.join(map(str, result)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
