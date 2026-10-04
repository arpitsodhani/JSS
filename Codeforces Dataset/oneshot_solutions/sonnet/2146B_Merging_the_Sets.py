import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        sets = []
        freq = [0] * (m + 1)
        
        for _ in range(n):
            k = data[idx]
            idx += 1
            cur = data[idx:idx + k]
            idx += k
            sets.append(cur)
            
            for x in cur:
                freq[x] += 1
        
        if any(freq[x] == 0 for x in range(1, m + 1)):
            answers.append("NO")
            continue
        
        removable = 0
        for cur in sets:
            can_remove = True
            for x in cur:
                if freq[x] == 1:
                    can_remove = False
                    break
            
            if can_remove:
                removable += 1
        
        answers.append("YES" if removable >= 2 else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
