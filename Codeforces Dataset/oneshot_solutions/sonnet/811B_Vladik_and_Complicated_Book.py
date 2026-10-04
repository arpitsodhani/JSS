import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    p = data[idx:idx + n]
    idx += n
    
    answers = []
    for _ in range(m):
        l = data[idx] - 1
        r = data[idx + 1] - 1
        x = data[idx + 2] - 1
        idx += 3
        
        value = p[x]
        smaller = 0
        for i in range(l, r + 1):
            if p[i] < value:
                smaller += 1
        
        if l + smaller == x:
            answers.append("Yes")
        else:
            answers.append("No")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
