import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    output = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        stack = []
        best = 0
        answers = []
        
        for _ in range(n):
            length = data[idx]
            value = data[idx + 1]
            idx += 2
            
            stack.append([value, length])
            
            while True:
                changed = False
                
                if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    stack[-2][1] += stack[-1][1]
                    stack.pop()
                    changed = True
                
                elif len(stack) >= 3 and stack[-1][0] == stack[-3][0]:
                    left_value, left_time = stack[-3]
                    mid_time = stack[-2][1]
                    right_time = stack[-1][1]
                    
                    if mid_time < left_time and mid_time < right_time:
                        new_time = left_time + right_time - mid_time
                        stack.pop()
                        stack.pop()
                        stack.pop()
                        stack.append([left_value, new_time])
                        changed = True
                
                if not changed:
                    break
            
            if stack[-1][1] > best:
                best = stack[-1][1]
            answers.append(str(best))
        
        output.append(' '.join(answers))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
