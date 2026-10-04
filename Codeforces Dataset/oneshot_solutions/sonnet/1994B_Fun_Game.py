import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        target = data[idx + 2]
        idx += 3
        
        first_s = s.find('1')
        first_t = target.find('1')
        
        if first_t == -1:
            answers.append("YES")
        elif first_s == -1 or first_t < first_s:
            answers.append("NO")
        else:
            answers.append("YES")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
