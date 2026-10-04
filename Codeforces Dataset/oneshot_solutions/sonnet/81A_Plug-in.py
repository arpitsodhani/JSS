import sys

def main():
    s = sys.stdin.readline().strip()
    
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    print(''.join(stack))

main()
