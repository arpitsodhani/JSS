import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        
        stacks = []
        for _ in range(3):
            stacks.append(data[idx:idx + n])
            idx += n
        
        knowledge = 0
        
        for stack in stacks:
            for value in stack:
                if value | x != x:
                    break
                knowledge |= value
        
        answers.append("Yes" if knowledge == x else "No")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
