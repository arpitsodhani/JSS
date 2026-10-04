import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    answers = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        c = data[idx + 2]
        idx += 3
        
        ok = True
        for x, y, z in zip(a, b, c):
            if z != x and z != y:
                ok = False
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
