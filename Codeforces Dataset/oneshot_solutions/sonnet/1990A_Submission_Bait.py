import sys
from collections import Counter

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
        
        count = Counter(a)
        winner = False
        
        for value in sorted(count):
            if count[value] % 2 == 1:
                winner = True
                break
        
        answers.append("YES" if winner else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
