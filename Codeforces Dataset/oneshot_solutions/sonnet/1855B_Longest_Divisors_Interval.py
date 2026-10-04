import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        length = 1
        while n % (length + 1) == 0:
            length += 1
        
        answers.append(str(length))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
