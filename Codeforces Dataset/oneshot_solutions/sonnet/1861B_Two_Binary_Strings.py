import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    answers = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        
        ok = False
        for i in range(len(a) - 1):
            if a[i] == b[i] == '0' and a[i + 1] == b[i + 1] == '1':
                ok = True
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
