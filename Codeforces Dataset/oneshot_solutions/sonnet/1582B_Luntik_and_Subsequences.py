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
        
        zeros = 0
        ones = 0
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            if x == 0:
                zeros += 1
            elif x == 1:
                ones += 1
        
        answers.append(str(ones * (1 << zeros)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
