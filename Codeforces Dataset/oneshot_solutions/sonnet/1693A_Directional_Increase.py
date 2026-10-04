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
        
        prefix = 0
        possible = True
        stopped = False
        
        for i in range(n):
            x = int(data[idx])
            idx += 1
            
            if stopped and x != 0:
                possible = False
            
            prefix += x
            
            if prefix < 0:
                possible = False
            
            if i < n - 1 and prefix == 0:
                stopped = True
        
        if prefix != 0:
            possible = False
        
        answers.append("Yes" if possible else "No")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
