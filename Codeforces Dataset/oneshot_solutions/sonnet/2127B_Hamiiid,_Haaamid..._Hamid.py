import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        left_wall = 0
        for i in range(x - 2, -1, -1):
            if s[i] == '#':
                left_wall = i + 1
                break
        
        right_wall = n + 1
        for i in range(x, n):
            if s[i] == '#':
                right_wall = i + 1
                break
        
        def cost(pos):
            if pos == 0 or pos == n + 1:
                return 1
            return 1 + min(pos, n - pos + 1)
        
        best = 0
        can_build = False
        
        for b in range(1, n + 1):
            if b == x or s[b - 1] == '#':
                continue
            
            can_build = True
            l = left_wall
            r = right_wall
            
            if b < x:
                l = max(l, b)
            else:
                r = min(r, b)
            
            best = max(best, min(cost(l), cost(r)))
        
        if not can_build:
            best = min(cost(left_wall), cost(right_wall))
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
