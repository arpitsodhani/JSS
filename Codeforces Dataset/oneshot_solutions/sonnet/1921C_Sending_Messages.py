import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        f = int(data[idx + 1])
        a = int(data[idx + 2])
        b = int(data[idx + 3])
        idx += 4
        
        prev = 0
        need = 0
        
        for _ in range(n):
            m = int(data[idx])
            idx += 1
            
            need += min((m - prev) * a, b)
            prev = m
        
        answers.append("YES" if need < f else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
