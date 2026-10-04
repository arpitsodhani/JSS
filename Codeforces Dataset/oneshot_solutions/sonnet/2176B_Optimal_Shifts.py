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
        
        if s.count('1') == n:
            answers.append("0")
            continue
        
        doubled = s + s
        max_gap = 0
        current = 0
        
        for c in doubled:
            if c == '0':
                current += 1
                max_gap = max(max_gap, current)
            else:
                current = 0
        
        max_gap = min(max_gap, n)
        answers.append(str(max_gap))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
