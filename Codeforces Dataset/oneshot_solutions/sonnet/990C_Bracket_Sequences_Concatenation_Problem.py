import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    positive = defaultdict(int)
    negative = defaultdict(int)
    balanced = 0
    
    for s in data[1:n + 1]:
        balance = 0
        min_prefix = 0
        
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            min_prefix = min(min_prefix, balance)
        
        if balance >= 0:
            if min_prefix == 0:
                if balance == 0:
                    balanced += 1
                else:
                    positive[balance] += 1
        else:
            if min_prefix >= balance:
                negative[-balance] += 1
    
    answer = balanced * balanced
    for need, count in positive.items():
        answer += count * negative[need]
    
    print(answer)

if __name__ == "__main__":
    main()
