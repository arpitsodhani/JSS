import sys

def can_transform(n, s, t):
    if s.replace('b', '') != t.replace('b', ''):
        return False
    
    s_a = []
    t_a = []
    s_c = []
    t_c = []
    
    for i in range(n):
        if s[i] == 'a':
            s_a.append(i)
        elif s[i] == 'c':
            s_c.append(i)
        
        if t[i] == 'a':
            t_a.append(i)
        elif t[i] == 'c':
            t_c.append(i)
    
    for x, y in zip(s_a, t_a):
        if x > y:
            return False
    
    for x, y in zip(s_c, t_c):
        if x < y:
            return False
    
    return True

def main():
    data = sys.stdin.read().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    
    ans = []
    for _ in range(q):
        n = int(data[idx])
        s = data[idx + 1]
        t = data[idx + 2]
        idx += 3
        
        ans.append("YES" if can_transform(n, s, t) else "NO")
    
    print('\n'.join(ans))

if __name__ == "__main__":
    main()
