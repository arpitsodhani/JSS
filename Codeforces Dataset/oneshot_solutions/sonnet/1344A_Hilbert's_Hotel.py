import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        seen = set()
        ok = True
        
        for i in range(n):
            a = int(data[idx])
            idx += 1
            
            room_class = (i + a) % n
            if room_class in seen:
                ok = False
            seen.add(room_class)
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
