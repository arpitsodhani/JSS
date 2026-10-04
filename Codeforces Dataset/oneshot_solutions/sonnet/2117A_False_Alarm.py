import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        
        doors = data[idx:idx + n]
        idx += n
        
        closed = [i for i, v in enumerate(doors) if v == 1]
        
        if not closed:
            answers.append("YES")
        elif closed[-1] - closed[0] + 1 <= x:
            answers.append("YES")
        else:
            answers.append("NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
