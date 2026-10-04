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
        
        c = data[idx:idx + n]
        idx += n
        c.sort()
        
        if c[0] != 1:
            answers.append("NO")
            continue
        
        total = 1
        possible = True
        
        for i in range(1, n):
            if c[i] > total:
                possible = False
                break
            total += c[i]
        
        answers.append("YES" if possible else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
