import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        has_left = has_right = False
        has_down = has_up = False
        
        for _ in range(n):
            x = data[idx]
            y = data[idx + 1]
            idx += 2
            
            if x < 0:
                has_left = True
            if x > 0:
                has_right = True
            if y < 0:
                has_down = True
            if y > 0:
                has_up = True
        
        if has_left and has_right and has_down and has_up:
            answers.append("NO")
        else:
            answers.append("YES")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
