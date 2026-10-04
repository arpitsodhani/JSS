import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    
    if len(data) == 1:
        token = data[0]
        i = 0
        while i < len(token) and token[i].isdigit():
            i += 1
        n = int(token[:i])
        s = token[i:]
    else:
        n = int(data[0])
        s = data[1]
    
    need = len(set(s))
    count = defaultdict(int)
    
    left = 0
    have = 0
    answer = n
    
    for right, ch in enumerate(s):
        if count[ch] == 0:
            have += 1
        count[ch] += 1
        
        while have == need:
            answer = min(answer, right - left + 1)
            old = s[left]
            count[old] -= 1
            if count[old] == 0:
                have -= 1
            left += 1
    
    print(answer)

if __name__ == "__main__":
    main()
