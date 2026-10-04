import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        best = 1
        current = 1
        
        for i in range(1, n):
            if s[i] == s[i - 1]:
                current += 1
            else:
                current = 1
            best = max(best, current)
        
        answers.append(str(best + 1))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
