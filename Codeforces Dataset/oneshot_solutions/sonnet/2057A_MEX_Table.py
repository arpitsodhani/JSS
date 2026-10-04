import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        answers.append(str(max(n, m) + 1))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
