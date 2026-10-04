import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]
    
    stack = []
    answer = 0
    
    for x in a:
        while stack and stack[-1] < x:
            answer = max(answer, stack[-1] ^ x)
            stack.pop()
        
        if stack:
            answer = max(answer, stack[-1] ^ x)
        
        stack.append(x)
    
    print(answer)

if __name__ == "__main__":
    main()
