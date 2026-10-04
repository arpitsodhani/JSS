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
        
        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            value = data[idx]
            idx += 1
            pos[value] = i
        
        operations = 0
        for value in range(1, n):
            if pos[value] > pos[value + 1]:
                operations += 1
        
        answers.append(str(operations))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
