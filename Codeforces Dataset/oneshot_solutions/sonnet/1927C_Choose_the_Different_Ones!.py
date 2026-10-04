import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        k = data[idx + 2]
        idx += 3
        
        a = set(data[idx:idx + n])
        idx += n
        b = set(data[idx:idx + m])
        idx += m
        
        only_a = 0
        only_b = 0
        both = 0
        
        possible = True
        for x in range(1, k + 1):
            in_a = x in a
            in_b = x in b
            
            if in_a and in_b:
                both += 1
            elif in_a:
                only_a += 1
            elif in_b:
                only_b += 1
            else:
                possible = False
                break
        
        half = k // 2
        if possible and only_a <= half and only_b <= half:
            answers.append("YES")
        else:
            answers.append("NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
