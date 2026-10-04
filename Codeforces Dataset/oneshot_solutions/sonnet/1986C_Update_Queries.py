import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        s = list(data[idx])
        idx += 1
        
        indices = []
        for _ in range(m):
            indices.append(int(data[idx]) - 1)
            idx += 1
        
        c = data[idx]
        idx += 1
        
        positions = sorted(set(indices))
        letters = sorted(c)
        
        for i, pos in enumerate(positions):
            s[pos] = letters[i]
        
        answers.append(''.join(s))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
