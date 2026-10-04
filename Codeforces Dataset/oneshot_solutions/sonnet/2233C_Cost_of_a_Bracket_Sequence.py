import sys

def solve_case(n, k, s):
    balance = 0
    pairs = 0
    before = [0] * n
    matched_close = [False] * n
    unmatched_close = [False] * n
    
    for i, c in enumerate(s):
        before[i] = balance
        if c == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
                pairs += 1
                matched_close[i] = True
            else:
                unmatched_close[i] = True
    
    critical_closes = []
    has_unmatched_after = False
    for i in range(n - 1, -1, -1):
        if s[i] == ')' and matched_close[i] and not has_unmatched_after:
            critical_closes.append(i)
        if unmatched_close[i]:
            has_unmatched_after = True
    critical_closes.reverse()
    
    critical_opens = []
    has_level_one_close = False
    for i in range(n - 1, -1, -1):
        if s[i] == '(' and has_level_one_close:
            critical_opens.append(i)
        if s[i] == ')' and before[i] == 1:
            has_level_one_close = True
    critical_opens.reverse()
    
    need = min(k, pairs)
    answer = ['0'] * n
    
    for pos in critical_closes:
        if need == 0:
            break
        answer[pos] = '1'
        need -= 1
    
    for pos in critical_opens:
        if need == 0:
            break
        answer[pos] = '1'
        need -= 1
    
    return ''.join(answer)

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        out.append(solve_case(n, k, s))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
