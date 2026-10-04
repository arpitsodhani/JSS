import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    
    if s.count('(') != s.count(')'):
        print(-1)
        return
    
    balance = 0
    start = -1
    answer = 0
    
    for i, ch in enumerate(s):
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance < 0 and start == -1:
            start = i
        
        if balance == 0 and start != -1:
            answer += i - start + 1
            start = -1
    
    print(answer)

if __name__ == "__main__":
    main()
