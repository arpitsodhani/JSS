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
        
        seen_decrease = False
        ok = True
        
        for i in range(1, n):
            if a[i] < a[i - 1]:
                seen_decrease = True
            elif seen_decrease and a[i] > a[i - 1]:
                ok = False
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
