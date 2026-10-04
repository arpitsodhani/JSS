import sys

def main():
    s = sys.stdin.read().strip()
    
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    opening = set('([{<')
    
    stack = []
    changes = 0
    
    for ch in s:
        if ch in opening:
            stack.append(ch)
        else:
            if not stack:
                print("Impossible")
                return
            
            top = stack.pop()
            if pairs[ch] != top:
                changes += 1
    
    if stack:
        print("Impossible")
    else:
        print(changes)

main()
