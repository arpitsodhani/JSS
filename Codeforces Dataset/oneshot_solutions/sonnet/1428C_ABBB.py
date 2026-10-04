import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    results = []
    for i in range(1, t + 1):
        s = data[i]
        stack = []
        
        for c in s:
            if c == 'B' and stack:
                stack.pop()
            else:
                stack.append(c)
        
        results.append(str(len(stack)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
