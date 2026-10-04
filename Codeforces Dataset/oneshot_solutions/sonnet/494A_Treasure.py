import sys

def main():
    s = sys.stdin.read().strip()
    
    positions = []
    balance = 0
    
    for c in s:
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
        else:
            positions.append(len(positions))
            balance -= 1
    
    if not positions:
        cur = 0
        for c in s:
            cur += 1 if c == '(' else -1
            if cur < 0:
                print(-1)
                return
        if cur == 0:
            return
        print(-1)
        return
    
    if balance < 0:
        print(-1)
        return
    
    result = [1] * len(positions)
    result[-1] += balance
    
    cur = 0
    idx = 0
    for c in s:
        if c == '(':
            cur += 1
        elif c == ')':
            cur -= 1
        else:
            cur -= result[idx]
            idx += 1
        
        if cur < 0:
            print(-1)
            return
    
    if cur != 0:
        print(-1)
        return
    
    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()
