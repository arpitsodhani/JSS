import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        max_left = -10**18
        min_right = 10**18
        
        for _ in range(n):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            
            max_left = max(max_left, l)
            min_right = min(min_right, r)
        
        answers.append(str(max(0, max_left - min_right)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
