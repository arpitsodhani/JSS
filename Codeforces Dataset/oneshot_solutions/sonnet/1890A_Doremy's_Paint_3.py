import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        count = Counter(a)
        
        if len(count) == 1:
            answers.append("Yes")
        elif len(count) == 2:
            values = list(count.values())
            if abs(values[0] - values[1]) <= 1:
                answers.append("Yes")
            else:
                answers.append("No")
        else:
            answers.append("No")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
