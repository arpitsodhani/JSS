def find_mex(s):
    n = len(s)
    
    # Try length 1
    chars = set(s)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in chars:
            return c
    
    # Try length 2
    substrings_2 = {s[i:i+2] for i in range(n-1)}
    for c1 in 'abcdefghijklmnopqrstuvwxyz':
        for c2 in 'abcdefghijklmnopqrstuvwxyz':
            candidate = c1 + c2
            if candidate not in substrings_2:
                return candidate
    
    # Try length 3
    substrings_3 = {s[i:i+3] for i in range(n-2)}
    for c1 in 'abcdefghijklmnopqrstuvwxyz':
        for c2 in 'abcdefghijklmnopqrstuvwxyz':
            for c3 in 'abcdefghijklmnopqrstuvwxyz':
                candidate = c1 + c2 + c3
                if candidate not in substrings_3:
                    return candidate

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(find_mex(s))
